import configparser

config_obj = configparser.ConfigParser()
config_obj.read('conf/application.conf')

# Configuration Constants
SERVER = "SERVER"
MONGO_DB_CREDENTIALS = "MONGO_DB_CREDENTIALS"
PORT_KEY = "PORT"
HOST_KEY = "HOST"

# SERVER Constants
PORT = config_obj.get(SERVER, PORT_KEY)
HOST = config_obj.get(SERVER, HOST_KEY)
# MONGO_URI = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_URI")
MONGO_DB_NAME = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_DB_NAME")
MONGO_COLLECTION_NAME = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_COLLECTION_NAME")
MONGO_HOST = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_HOST")
MONGO_PORT = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_PORT")
MONGO_USERNAME = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_USERNAME")
# MONGO_PASSWORD = config_obj.get(MONGO_DB_CREDENTIALS, "MONGO_PASSWORD")
