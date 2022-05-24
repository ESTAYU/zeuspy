#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

from zeuspy import __version__

from pygments.styles.friendly import FriendlyStyle

FriendlyStyle.background_color = "#f3f2f1"

project = "zeuspy"
copyright = f"2017-present, Dan"
author = "Dan"

version = ".".join(__version__.split(".")[:-1])

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton"
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"

templates_path = ["../resources/templates"]
html_copy_source = False

napoleon_use_rtype = False
napoleon_use_param = False

pygments_style = "friendly"

copybutton_prompt_text = "$ "

suppress_warnings = ["image.not_readable"]

html_title = "zeuspy Documentation"
html_theme = "sphinx_rtd_theme"
html_static_path = ["../resources/static"]
html_show_sourcelink = True
html_show_copyright = False
html_theme_options = {
    "canonical_url": "https://docs.zeuspy.org/",
    "collapse_navigation": True,
    "sticky_navigation": False,
    "logo_only": True,
    "display_version": False,
    "style_external_links": True
}

html_logo = "../resources/static/img/zeuspy.png"
html_favicon = "../resources/static/img/favicon.ico"

latex_engine = "xelatex"
latex_logo = "../resources/static/img/zeuspy.png"

latex_elements = {
    "pointsize": "12pt",
    "fontpkg": r"""
        \setmainfont{Open Sans}
        \setsansfont{Bitter}
        \setmonofont{Ubuntu Mono}
        """
}
