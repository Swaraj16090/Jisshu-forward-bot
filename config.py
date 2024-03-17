from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26558850")
    API_HASH = environ.get("API_HASH", "410f922c49c8867b5c8e28d624581b02")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6916120443:AAE0ahxPIFjR4JG84ePKYM-Wu-4ly455nLs") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://test08:test08@cluster0.jit72we.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1967990132').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
