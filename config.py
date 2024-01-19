import os

API_ID = API_ID = 20346550

API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6630488360:AAEruM7loQUEXy4chSToRowG0vvT8-1TEr4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6381511858))

LOG = -1002142081905

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6148938625").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


