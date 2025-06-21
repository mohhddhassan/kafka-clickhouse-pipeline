from kafka import KafkaProducer
from faker import Faker
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

fake = Faker()

while True:
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18, 60)
    }
    print("Sending:", data)
    producer.send("user-signups", value=data)
    time.sleep(1)