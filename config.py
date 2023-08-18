
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

patterns = {
    "PHONE_NUMBER": r'(?:\+90.?5|0090.?5|905|0?5)(?:[01345][0-9])\s?(?:[0-9]{3})\s?(?:[0-9]{2})\s?(?:[0-9]{2})',
    "ID": r'\b[1-9]{1}[0-9]{9}[02468]{1}',
    "CREDIT_CARD": r'\b(?:\d{4}[ -]?){3}\d{4}\b',
    "PLATE": r"\b\d{2} [A-Z]{1,3} \d{2,4}\b|\b\d{2} [A-Z]{2} \d{3}\b|\b\d{2} [A-Z]{3} \d{2,3}\b|\b\d{2}[A-Z]{3}\d{2}\b|\b\d{2}[A-Z]{2}\d{3}\b|\b\d{2}[A-Z]{1,3}\d{2,4}\b",
    "DATETIME": r'\b\d{2}[/\.]\d{2}[/\.]\d{4}\b',
    "E-MAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "DOMAIN": r'\b(?:https?://)?([A-Za-z_0-9.-]+(?:\.[A-Za-z]{2,})+)\b',
    "URL": r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    "MD5-HASH": r'\b[a-fA-F0-9]{32}\b',
    "SHA1-HASH": r'\b[a-fA-F0-9]{40}\b',
    "SHA256-HASH": r'\b[a-fA-F0-9]{64}\b',
    "COMBOLIST": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+[*:][^\s]+',
}

