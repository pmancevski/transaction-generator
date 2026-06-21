from kafka import KafkaProducer
import json

class KafkaProducerClient:
    def __init__(self, bootstrap_servers, api_key, api_secret, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            security_protocol='SASL_SSL',
            sasl_mechanism='PLAIN',
            sasl_plain_username=api_key,
            sasl_plain_password=api_secret,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def send(self, transaction):
        self.producer.send(self.topic, value=transaction)
        self.producer.flush()