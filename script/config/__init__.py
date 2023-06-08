from configparser import ConfigParser
import sys
import os.path

try:
    config = ConfigParser()
    config.read("conf/application.conf")
except Exception as e:
    print(f"Error while loading the config: {e}")
    print("Failed to Load Configuration. Exiting!!!")
    sys.stdout.flush()
    sys.exit()


class DBConf:
    MONGO_URI = config.get("MONGO_DB", "uri")
    if not MONGO_URI:
        print("Error, environment variable MONGO_URI not set")
        sys.exit(1)


class service_data():
    port = int(config.get("SERVICE", "port"))
    host = config.get("SERVICE", "host")
