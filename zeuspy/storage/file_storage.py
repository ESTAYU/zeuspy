#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import logging
import os
import sqlite3
from pathlib import Path

from .sqlite_storage import SQLiteStorage

log = logging.getLogger(__name__)


class FileStorage(SQLiteStorage):
    FILE_EXTENSION = ".session"

    def __init__(self, name: str, workdir: Path):
        super().__init__(name)

        self.database = workdir / (self.name + self.FILE_EXTENSION)

    def update(self):
        version = self.version()

        if version == 1:
            with self.lock, self.conn:
                self.conn.execute("DELETE FROM peers")

            version += 1

        if version == 2:
            with self.lock, self.conn:
                self.conn.execute("ALTER TABLE sessions ADD api_id INTEGER")

            version += 1

        self.version(version)

    async def open(self):
        path = self.database
        file_exists = path.is_file()

        self.conn = sqlite3.connect(str(path), timeout=1, check_same_thread=False)

        if not file_exists:
            self.create()
        else:
            self.update()

        with self.conn:
            try:  # Python 3.6.0 (exactly this version) is bugged and won't successfully execute the vacuum
                self.conn.execute("VACUUM")
            except sqlite3.OperationalError:
                pass

    async def delete(self):
        os.remove(self.database)
