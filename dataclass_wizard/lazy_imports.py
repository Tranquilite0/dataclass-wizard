"""
Lazy Import definitions. Generally, these imports will be available when any
"bonus features" are installed, i.e. as below:

  $ pip install dataclass-wizard[timedelta]
"""

# Tranquilite: Modified file to make library work when dynamically loaded in a cx_freeze environment
# which does not contain the tomllib package.
# Per the Apache 2.0 Licence: "You must cause any modified files to carry prominent notices stating that You changed the files"

from .constants import PY311_OR_ABOVE
from .utils.lazy_loader import LazyLoader


# python-dotenv: for loading environment values from `.env` files
dotenv = LazyLoader(globals(), "dotenv", "dotenv", local_name="python-dotenv")

# pytimeparse: for parsing JSON string values as a `datetime.timedelta`
pytimeparse = LazyLoader(globals(), "pytimeparse", "timedelta")

# PyYAML: to add support for (de)serializing YAML data to dataclass instances
yaml = LazyLoader(globals(), "yaml", "yaml", local_name="PyYAML")

# Tomli -or- tomllib (PY 3.11+): to add support for (de)serializing TOML
# data to dataclass instances
if PY311_OR_ABOVE:
    toml = LazyLoader(globals(), "tomllib", "toml", local_name="tomllib")
else:
    toml = LazyLoader(globals(), "tomli", "toml", local_name="tomli")

# Tomli-W: to add support for serializing dataclass instances to TOML
toml_w = LazyLoader(globals(), "tomli_w", "toml", local_name="tomli-w")
