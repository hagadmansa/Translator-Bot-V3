from plugins.admin import Database


BOT_OWNER = int(os.environ.get("BOT_OWNER"))
DATABASE = os.environ.get("DATABASE_URL")
db = Database(DATABASE)
DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "en")
