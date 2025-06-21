from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from faker import Faker
import json, time, random

KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092'

# Retry logic to wait for Kafka broker to be ready
for i in range(10):  # Try up to 10 times
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("✅ Connected to Kafka broker.")
        break
    except NoBrokersAvailable:
        print(f"❌ Kafka broker not available, retrying in 5 seconds... ({i+1}/10)")
        time.sleep(5)
else:
    print("❌ Kafka broker not available after 10 retries. Exiting.")
    exit(1)

# Now start producing fake data
fake = Faker()

while True:
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18, 60)
    }
    print("📤 Sending:", data)
    producer.send("user-signups", value=data)
    time.sleep(1)
