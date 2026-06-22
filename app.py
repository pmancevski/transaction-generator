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
    
    # # Send one transaction
    # transaction = generator.generate()
    # print(f"transaction: {transaction}")
    # producer.send(transaction)
    # print(f"Sent: {transaction['transactionId']}")
    
    
    # Uncomment to run continuously every 30 seconds
    while True:
        transaction = generator.generate()
        producer.send(transaction)
        print(f"Sent: {transaction['transactionId']} | User: {transaction['userId']} | Location: {transaction['location']} | Amount: {transaction['amount']}")
        time.sleep(5)

if __name__ == "__main__":
    main()