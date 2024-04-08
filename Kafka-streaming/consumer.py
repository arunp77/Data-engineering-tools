from kafka import KafkaConsumer
import ast
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

kafka_consumer = KafkaConsumer(
    "twitter",
    bootstrap_servers="<your_vm_ip_addr>",
    auto_offset_reset="earliest"
)

def print_dict(dict_):
    for key in dict_.keys():
        print(f"{key}: {dict_[key]}")

for message in kafka_consumer:
    # print(message.value[:20], end="")
    dict_tweet = json.loads(message.value)
    score = sentiment_analyzer.polarity_scores(dict_tweet["text"])["compound"]
    print(f"SCORE: {score}")
    # col.insert_one(dict_)
    with open("sentiment_scores.txt", "a") as file:
        file.write(str(score) + "\n")
