-- Kafka engine table (temporary buffer)
CREATE TABLE kafka_queue (
  name String,
  email String,
  age UInt8
) ENGINE = Kafka
SETTINGS
  kafka_broker_list = 'kafka:9092',
  kafka_topic_list = 'user-signups',
  kafka_format = 'JSONEachRow',
  kafka_group_name = 'clickhouse-consumer';

-- Final MergeTree table to store the data
CREATE TABLE users (
  name String,
  email String,
  age UInt8
) ENGINE = MergeTree()
ORDER BY name;

-- Materialized view to auto-insert Kafka data into users table
CREATE MATERIALIZED VIEW consume_kafka TO users AS
SELECT * FROM kafka_queue;
