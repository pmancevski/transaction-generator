from transaction import generate_transaction
import random

class TransactionGenerator:
    def __init__(self):
        self.users = {}
        self.location_patterns = {}
        self.velocity_patterns = {}

    def generate(self):
        # 50% chance to trigger a pattern
        if random.random() < 0.5:
            return self.generate_patterned_transaction()
        else:
            return generate_transaction()

    def generate_patterned_transaction(self):
        pattern = random.choice(["velocity", "location"])
        
        if pattern == "velocity":
            return self.generate_velocity_pattern()
        else:
            return self.generate_location_pattern()

    def generate_velocity_pattern(self):
        # Same user, 4+ transactions in a short time
        print("Velocity pattern activated")
        user_id = random.choice(["user_velocity_1", "user_velocity_2", "user_velocity_3"])
        count = self.velocity_patterns.get(user_id, 0) + 1
        self.velocity_patterns[user_id] = count

        tx = generate_transaction()
        tx["userId"] = user_id
        tx["amount"] = round(random.uniform(100, 5000), 2)

        if count >= 4:
            # Reset after triggering
            self.velocity_patterns[user_id] = 0
            # Make one of them high amount to trigger both rules
            tx["amount"] = round(random.uniform(15000, 25000), 2)

        return tx

    def generate_location_pattern(self):
        # Same user, different locations
        print("Location pattern activated")
        user_id = random.choice(["user_location_1", "user_location_2"])
        locations = ["US", "GB", "FR", "DE", "IT", "ES", "CA", "AU", "JP", "BR"]

        count = self.location_patterns.get(user_id, 0)
        self.location_patterns[user_id] = count + 1

        tx = generate_transaction()
        tx["userId"] = user_id
        tx["location"] = locations[count % len(locations)]

        if count >= 3:
            # Reset after triggering
            self.location_patterns[user_id] = 0

        return tx