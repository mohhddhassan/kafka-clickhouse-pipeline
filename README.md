
<<<<<<< HEAD
---

=======
>>>>>>> origin/master
# ⚡ Kafka to ClickHouse Data Pipeline

Hey! I'm Mohamed Hussain — currently working as an **Associate Data Engineer Intern** 👨‍💻
This repo is my attempt at building a **lightweight real-time pipeline** using **Kafka + ClickHouse** — ideal for beginners stepping into the world of streaming and OLAP systems.

If you're curious about how data flows in real-time pipelines, this simple project might help 🎯

---

## 📁 Project Structure

| Folder               | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| `producer/`          | Python app that generates data and sends it to Kafka and ClickHouse |
| `clickhouse-init/`   | SQL script to create the required table in ClickHouse               |
| `screenshots/`       | Visual proof — architecture diagram, Kafka topic, ClickHouse output |
| `docker-compose.yml` | Docker setup to spin up Kafka, Zookeeper, and ClickHouse            |
| `README.md`          | You’re reading it!                                                  |

---

## 🚀 What This Does

* The **producer** generates mock website visit logs (timestamp, URL, country)
* It pushes each record into a **Kafka** topic named `website_visits`
* Simultaneously, the same data is also inserted into a **ClickHouse** table
* All services (Kafka, Zookeeper, ClickHouse) run inside Docker

---

## 🎯 Why I Did This

* Understand how real-time systems like **Kafka** and **ClickHouse** interact
* Learn how to write and run a Kafka producer in Python
* Explore OLAP-style storage with ClickHouse
* Build something small but useful ✨

---

## 🧠 Key Takeaways

* How Kafka brokers and topics work with Python producers
* How to insert records into ClickHouse using Python
* How Docker simplifies environment setup
* How to model basic OLAP tables for real-time ingestion

---

## 🔧 What's Next?

* Add a **Kafka consumer** that reads and inserts into ClickHouse (classic architecture)
* Add logging and error-handling middleware
* Simulate more complex streaming use cases (e.g., log aggregation)
* Add Grafana to visualize real-time metrics from ClickHouse 📊

---

## 🙌 Thanks To

* [ClickHouse](https://clickhouse.com/docs/en/) for the fast OLAP database
* [Confluent Kafka Python](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html) for the Kafka client
* ClickHouse + Kafka community examples for inspiration

---

## 👋 About Me

**Mohamed Hussain S**
Associate Data Engineer Intern
[LinkedIn](https://linkedin.com/in/hussainmohhdd) | [GitHub](https://github.com/mohhddhassan)

---

> Building in public — one stream at a time ⚙️