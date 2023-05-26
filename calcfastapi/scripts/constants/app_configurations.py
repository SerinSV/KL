import configparser

config_obj = configparser.ConfigParser()
config_obj.read('configuration/application.conf')

# Configuration Constants
SERVER = "SERVER"
PORT_KEY = "PORT"
HOST_KEY = "HOST"

# SERVER Constants
PORT = config_obj.get(SERVER, PORT_KEY)
HOST = config_obj.get(SERVER, HOST_KEY)
