"""
Simple kakfa producer with python kafka library
"""

from kafka import KafkaProducer
import time
import json


# Read config file
producer_config_fd = open('config.json', "r")
producer_config = json.load(producer_config_fd)

# Parse configs from file to get desired value
bootstrap_servers=producer_config.get('bootstrap_servers')
security_protocol=producer_config.get('security_protocol')


# Create and Configuring the Kafka producer 
producer = KafkaProducer(
     	bootstrap_servers=bootstrap_servers,
)

TOPIC_NAME='python_producer_1'


## Generate many messages in total with 1 second interval
for i in range(3):
      
      message = f"Python client Hello: {i + 1}!"

      # Publish a message to a topic, (Create new topic if not exists).      
      producer.send(TOPIC_NAME, message.encode('utf-8'))
      
      print(f"Message sent: {message}")
      time.sleep(1)

# destroy producer object
producer.close()




