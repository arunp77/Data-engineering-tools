# Data Processing Engine with Kafka, S3, and Athena
This is a summary of the video: [https://www.youtube.com/watch?v=KerNf0NANMo](https://www.youtube.com/watch?v=KerNf0NANMo)
## Introduction
- **Objectives**: Use Python to produce stock market data, send it to a Kafka cluster, consume the data, store it in Amazon S3, crawl the data to build an AWS Glue catalog, and analyze the data using Amazon Athena.
- **Video Structure**: The video is divided into three parts: prerequisites, basics of Kafka, and hands-on practice.
- **Speaker**: My name is Sarthak, a freelance data engineer focused on data engineering, productivity, and freelancing.

## Prerequisites
- Laptop and internet connection for browser and cloud machine operations.
- Python (>3.5) installed on a PC/laptop and basic understanding of Python.
- AWS account for S3 storage, EC2 Kafka servers, Glue crawler, and Athena queries.
- Jupyter Notebook installed for writing Python code.

## Part 1: Basics of Kafka
### What is Kafka?
- **Definition**: Apache Kafka is a distributed event store and stream processing platform.
- **Real-time Streaming**: Utilized in applications like Google Maps, Uber, Amazon, where events are processed in real-time.
- **Components**:
  - **Producer**: Generates data (e.g., sensors, web analytics).
  - **Broker**: Server nodes in a Kafka cluster.
  - **Consumer**: Consumes data from Kafka brokers.
  - **Zookeeper**: Manages configuration, synchronization, and failures within the Kafka cluster.
  - **Topics**: Logical data storage units in Kafka brokers, which can be split into partitions for better manageability and performance.

### Kafka Architecture
- Kafka has multiple producers and consumers connected to Kafka servers (brokers) within a cluster managed by Zookeeper.
- Data from producers is sent to topics (logical data units) that consist of partitions.
- **Replication**: Data is replicated across multiple brokers to ensure fault tolerance.

## Part 2: Hands-On Setup
### Setting Up Kafka on EC2
1. **Launch EC2 Instance**: Amazon Linux, T2.micro (free tier), create a key pair for SSH access.
2. **Connect to EC2 Instance** via SSH.
3. **Install Java**: `sudo yum install java-1.8.0-openjdk`.
4. **Download and Extract Kafka**: Use wget to download Kafka and then extract it.
5. **Start Zookeeper**: `bin/zookeeper-server-start.sh config/zookeeper.properties`
6. **Start Kafka Server**: `bin/kafka-server-start.sh config/server.properties`

### Configuring Public IP
- Modify Kafka configuration to use the public IP of the EC2 instance instead of the private IP to enable external access.

### Creating Topics and Testing
1. **Create Kafka Topic**: `bin/kafka-topics.sh --create --topic demo --bootstrap-server <public-ip>:9092`
2. **Start Producer**: `bin/kafka-console-producer.sh --topic demo --bootstrap-server <public-ip>:9092`
3. **Start Consumer**: `bin/kafka-console-consumer.sh --topic demo --bootstrap-server <public-ip>:9092`
- Verify the data flow between producer and consumer.

## Part 3: Python Code Implementation
### Setting Up Python Code
- **Install Kafka-Python**: `pip install kafka-python`

### Kafka Producer Code
- **Imports**: `pandas`, `KafkaProducer`, `time`, `json`
- **Producer Object**:
```python
producer = KafkaProducer(bootstrap_servers=['<public-ip>:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
```
- **Send Data Example**:
```python
producer.send('demo', value={'name': 'Sarthak'})
```

### Kafka Consumer Code
- **Consumer Object**:
```python
consumer = KafkaConsumer('demo', bootstrap_servers=['<public-ip>:9092'], auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
```
- **Consume Data Example**:
```python
for message in consumer:
    print(message.value)
```

### Streaming Stock Market Data
- **Simulate Real-time Data**: Use an existing CSV dataset and send random samples to Kafka.
- **Producer Code for Streaming**:
```python
import pandas as pd
data = pd.read_csv('stock_data.csv')
while True:
    sample = data.sample(1).to_dict(orient='records')[0]
    producer.send('stock_topic', value=sample)
    time.sleep(1)
```

## Part 4: Storing Data in Amazon S3
### Configure AWS on Local Machine
- **Install AWS CLI**: Follow instructions on the AWS website.
- **Configure AWS CLI**: `aws configure` and provide access key, secret key, region, and default output format.

### S3 Integration in Python
- **Install S3FS**: `pip install s3fs`
- **Upload Data from Consumer to S3**:
```python
s3 = S3FileSystem()
for count, message in enumerate(consumer):
    with s3.open(f's3://<bucket-name>/data_{count}.json', 'w') as file:
        file.write(json.dumps(message.value))
```

## Part 5: AWS Glue and Athena
### Setting Up Glue Crawler
1. **Create a Glue Crawler**: Define data source and IAM Role to access S3.
2. **Run the Crawler**: Create schema in Glue Data Catalog.

### Querying Data with Athena
- Use Athena to query real-time data stored in S3.
- Example Query: `SELECT * FROM <table-name> LIMIT 10;`

## Conclusion
- Successfully created a real-time data processing engine using Apache Kafka, AWS S3, Glue, and Athena.
- **Next Steps**:
  - Explore more on Kafka, different types of consumers, and connectors.
  - Integration with other databases or real-time dashboards.
- **Tips**: Don’t give up if you encounter errors. Try to troubleshoot on your own before seeking help.

## Supporting the Channel
- Make sure to like, subscribe, and leave comments if you found this useful!
