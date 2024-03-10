"""
Simple kakfa consumer with python kafka library
"""

from kafka import KafkaConsumer
import json

# Read config file
consumer_config_fd = open('config.json', "r")
consumer_config = json.load(consumer_config_fd)

# Parse configs from file to get desired value
bootstrap_servers=consumer_config.get('bootstrap_servers')
security_protocol=consumer_config.get('security_protocol')

TOPIC_TO_CONSUME='python_producer_1'

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(TOPIC_TO_CONSUME,
                         auto_offset_reset="earliest",
                         bootstrap_servers=bootstrap_servers)

# Continuously poll for new messages
for msg in consumer:
  print("Message: ", msg.value)

