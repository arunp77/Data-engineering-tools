from kafka import KafkaProducer
from tqdm import tqdm
import json
import time
import random

kafka_producer = KafkaProducer(bootstrap_servers="<your_vm_ip_addr>")

path = "large_tweets.json"

with open(path, "r") as file:
    tweets = json.load(file)

n_tweets = len(tweets)

for i in tqdm(range(1, 3000)):
    time.sleep(0.5)
    kafka_producer.send(
        topic="twitter",
        value=json.dumps(tweets[random.randint(0, n_tweets) - 1]).encode("utf-8"),
    )

kafka_producer.flush()
