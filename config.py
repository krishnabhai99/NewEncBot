import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("26387127", "")  # ⚠️ Required
    API_HASH  = os.environ.get("19718ab7acd97d0f71ada2807ddfe47a", "") # ⚠️ Required
    BOT_TOKEN = os.environ.get("7713467145:AAH4U81n9mgM0ICZyXzT_dZeRzlRxAUdy5g", "") # ⚠️ Required
    FORCE_SUB = os.environ.get('-1002289711537', '') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("5446367898", "0")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('-1002317509038', '0')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph//file/80a97e703fc3fdbcaefc5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
