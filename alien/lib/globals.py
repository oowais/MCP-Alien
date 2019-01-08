import os

# Common
LOGGER_TAG = "alien"

# External MQTT Address
EXTERNAL_BROKER_HOST = "localhost" # testing, to be removed
#EXTERNAL_BROKER_HOST = "terrarium"
EXTERNAL_BROKER_PORT = 1883

# Backdoor Auth
AUTH_INFO_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "auth_info")
KEEP_STREAM_TIME = 120

# GPIO Setup
MIN_DUTY = 3
MAX_DUTY = 11
CENTER = (MAX_DUTY + MIN_DUTY) / 2
CHANNEL_FREQ = 50

# Movement Setup
WALKING_PINS = [("left_leg", 2), ("left_foot", 3), ("right_leg", 4), ("right_foot", 17)]
