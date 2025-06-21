

# ⚡ Kafka → ClickHouse: Real-Time Data Pipeline

> A beginner-friendly real-time pipeline using Kafka, Python, and ClickHouse — containerized with Docker.

Hey! I'm Mohamed Hussain — currently working as an **Associate Data Engineer Intern** 👨‍💻
This repo is my attempt at building a **lightweight real-time pipeline** using **Kafka + ClickHouse** — ideal for beginners stepping into the world of streaming and OLAP systems.

If you're curious about how data flows in real-time pipelines, this simple project might help 🎯

---

## 📁 Project Structure

| Folder / File          | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| `producer/`            | Python app that generates and sends mock user data to Kafka                |
| `clickhouse-setup.sql` | SQL file to set up Kafka engine table, target table, and materialized view |
| `docker-compose.yml`   | Docker setup to run Kafka, Zookeeper, and ClickHouse                       |
| `screenshots/`         | Visual proof — architecture diagram, Kafka topic, ClickHouse output        |
| `README.md`            | You're reading it! 📖                                                      |

---

## 🚀 What This Does

* Generates mock user data (`name`, `email`, `age`) using Python
* Pushes each record to a **Kafka** topic named `user-signups`
* **ClickHouse** consumes the topic via `Kafka` engine table and materialized view
* All services run in **Docker** for easy setup and teardown

---

## 🎯 Why I Did This

* Understand how real-time systems like **Kafka** and **ClickHouse** interact
* Learn how to write a **Kafka Producer** using Python
* Explore **ClickHouse’s Kafka integration** and materialized views
* Build something real-world yet lightweight ✨

---

## 🧠 Key Takeaways

* How Kafka topics and brokers work with Python producers
* How ClickHouse can consume from Kafka directly using **engine tables**
* How to structure and run real-time ingestion pipelines
* How Docker simplifies environment orchestration

---

## ⚙️ How To Run

```bash
# Step 1: Clone this repo
git clone https://github.com/mohhddhassan/kafka-clickhouse-pipeline.git
cd kafka-clickhouse-pipeline

# Step 2: Start Docker containers
docker-compose up -d

# Step 3: Apply the ClickHouse setup
# Connect to ClickHouse and run the SQL script inside the container
docker exec -it clickhouse clickhouse-client < clickhouse-setup.sql

# Step 4: Run the Kafka producer
cd producer
python producer.py
```

---

## 🧪 Example Output

Once the pipeline is running:

* Kafka topic will receive messages like:

  ```json
  {"name": "Alice", "email": "alice@example.com", "age": 24}
  ```

* ClickHouse table `users` will store the data automatically via a materialized view

Check the `screenshots/` folder to see example output from ClickHouse CLI and Kafka console.

---

## 🔧 What's Next?

* Add a proper **Kafka consumer** as an alternative to ClickHouse's internal consumption
* Add **logging**, retries, and dead-letter queues
* Simulate more complex streaming use cases (e.g., page visits, e-commerce logs)
* Add **Grafana** dashboard for real-time visualization 📊

> Have an idea or feedback? Feel free to fork and contribute! 🚀

---

## 🙌 Thanks To

* [ClickHouse](https://clickhouse.com/docs/en/) — the insanely fast OLAP database
* [Confluent Kafka Python](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
* Open-source communities for Kafka + ClickHouse integration examples

---

## 👋 About Me

**Mohamed Hussain S**
Associate Data Engineer Intern
[LinkedIn](https://linkedin.com/in/hussainmohhdd) | [GitHub](https://github.com/mohhddhassan)

---

> Building in public — one stream at a time ⚙️

---

