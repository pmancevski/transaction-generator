from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_transaction():
    return {
        "transactionId": f"txn_{fake.uuid4()[:8]}",
        "userId": f"user_{fake.uuid4()[:8]}",
        "amount": round(random.uniform(10, 20000), 2),
        "currency": random.choice(["USD", "EUR", "GBP", "CAD"]),
        "location": fake.country_code(),
        "deviceId": f"device_{fake.uuid4()[:8]}",
        "timestamp": datetime.now().isoformat(),
        "merchant": fake.company()
    }