# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "23980376"))
API_HASH = getenv("API_HASH", "2aca0baab7f8ec9b445a248e8403cc98")
BOT_TOKEN = getenv("BOT_TOKEN", "7638791270:AAGpYviS-ovI1EEs3a4ybhucY27oHElNHFQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "itschangir").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://atlas-sample-dataset-load-67fb73692a23d632b310c3cb:jCdKC0Yuqa2mmUVp@cluster0.en0o1f9.mongodb.net/?")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/logjiaao1")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2597544812"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
