#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import os
import re
from datetime import datetime
from typing import Union, BinaryIO, List, Optional, Callable

import zeuspy
from zeuspy import StopTransmission, enums
from zeuspy import raw
from zeuspy import types
from zeuspy import utils
from zeuspy.errors import FilePartMissing
from zeuspy.file_id import FileType


class SendVoice:
    async def send_voice(
        self: "zeuspy.Client",
        chat_id: Union[int, str],
        voice: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        duration: int = 0,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Send audio files.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            voice (``str`` | ``BinaryIO``):
                Audio file to send.
                Pass a file_id as string to send an audio that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get an audio from the Internet,
                pass a file path as string to upload a new audio that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            caption (``str``, *optional*):
                Voice message caption, 0-1024 characters.

            parse_mode (:obj:`~zeuspy.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~zeuspy.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            duration (``int``, *optional*):
                Duration of the voice message in seconds.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            reply_markup (:obj:`~zeuspy.types.InlineKeyboardMarkup` | :obj:`~zeuspy.types.ReplyKeyboardMarkup` | :obj:`~zeuspy.types.ReplyKeyboardRemove` | :obj:`~zeuspy.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            :obj:`~zeuspy.types.Message` | ``None``: On success, the sent voice message is returned, otherwise, in
            case the upload is deliberately stopped with :meth:`~zeuspy.Client.stop_transmission`, None is returned.

        Example:
            .. code-block:: python

                # Send voice note by uploading from local file
                await app.send_voice("me", "voice.ogg")

                # Add caption to the voice note
                await app.send_voice("me", "voice.ogg", caption="voice caption")

                # Set voice note duration
                await app.send_voice("me", "voice.ogg", duration=20)
        """
        file = None

        try:
            if isinstance(voice, str):
                if os.path.isfile(voice):
                    file = await self.save_file(voice, progress=progress, progress_args=progress_args)
                    media = raw.types.InputMediaUploadedDocument(
                        mime_type=self.guess_mime_type(voice) or "audio/mpeg",
                        file=file,
                        attributes=[
                            raw.types.DocumentAttributeAudio(
                                voice=True,
                                duration=duration
                            )
                        ]
                    )
                elif re.match("^https?://", voice):
                    media = raw.types.InputMediaDocumentExternal(
                        url=voice
                    )
                else:
                    media = utils.get_input_media_from_file_id(voice, FileType.VOICE)
            else:
                file = await self.save_file(voice, progress=progress, progress_args=progress_args)
                media = raw.types.InputMediaUploadedDocument(
                    mime_type=self.guess_mime_type(voice.name) or "audio/mpeg",
                    file=file,
                    attributes=[
                        raw.types.DocumentAttributeAudio(
                            voice=True,
                            duration=duration
                        )
                    ]
                )

            while True:
                try:
                    r = await self.invoke(
                        raw.functions.messages.SendMedia(
                            peer=await self.resolve_peer(chat_id),
                            media=media,
                            silent=disable_notification or None,
                            reply_to_msg_id=reply_to_message_id,
                            random_id=self.rnd_id(),
                            schedule_date=utils.datetime_to_timestamp(schedule_date),
                            noforwards=protect_content,
                            reply_markup=await reply_markup.write(self) if reply_markup else None,
                            **await utils.parse_text_entities(self, caption, parse_mode, caption_entities)
                        )
                    )
                except FilePartMissing as e:
                    await self.save_file(voice, file_id=file.id, file_part=e.value)
                else:
                    for i in r.updates:
                        if isinstance(i, (raw.types.UpdateNewMessage,
                                          raw.types.UpdateNewChannelMessage,
                                          raw.types.UpdateNewScheduledMessage)):
                            return await types.Message._parse(
                                self, i.message,
                                {i.id: i for i in r.users},
                                {i.id: i for i in r.chats},
                                is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage)
                            )
        except StopTransmission:
            return None
