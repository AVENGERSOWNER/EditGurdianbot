import os

API_ID = int(os.getenv("API_ID", "4014305"))
API_HASH = os.getenv("API_HASH", "b0cb9e17b2b8bcde3be7161c8bfa6013")

# Telegram bot token
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7614975010:AAFRSSPowfzrOfCfgKE0xAD0FmEMhZZ8JFE")

# Your telegram user ID (owner)
OWNER_ID = int(os.getenv("OWNER_ID", "5817544006"))

# Sudo users (comma separated in Heroku config)
SUDO_ID = list(map(int, os.getenv("SUDO_ID", "1669178360,7642159940,6128266949").split(",")))

# MongoDB connection
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority"
)

DB_NAME = os.getenv("DB_NAME", "Nullcrow")

LOGGER = os.getenv("LOGGER", "True").lower() in ["true", "1", "yes"]

BOT_NAME = os.getenv("BOT_NAME", "Edit Guardian")

SUPPORT_ID = int(os.getenv("SUPPORT_ID", "-1001515594503"))
