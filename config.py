import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_CONFIG = {
    "bootstrap_servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "api_key": os.getenv("KAFKA_API_KEY"),
    "api_secret": os.getenv("KAFKA_API_SECRET"),
    "topic": os.getenv("KAFKA_TOPIC")
}