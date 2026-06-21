from dotenv import load_dotenv
import os
from generator import TransactionGenerator
from producer import KafkaProducerClient
import time

load_dotenv()

def main():
    producer = KafkaProducerClient(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
        api_key=os.getenv("KAFKA_API_KEY"),
        api_secret=os.getenv("KAFKA_API_SECRET"),
        topic=os.getenv("KAFKA_TOPIC")
    )
    
    generator = TransactionGenerator()
    
    print("Starting transaction generator...")
    print(f"Sending to topic: {os.getenv('KAFKA_TOPIC')}")
    
    while True:
        transaction = generator.generate()
        producer.send(transaction)
        print(f"Sent: {transaction['transactionId']}")
        time.sleep(2)

if __name__ == "__main__":
    main()