# Import the required library
from kafka import KafkaConsumer

# Configuring the Kafka consumer  
consumer = KafkaConsumer(
    "testssl-topic",
    auto_offset_reset="earliest",
    bootstrap_servers=f"kafka.kifarunix-demo.com:9092", # From the connection information for the managed service
    security_protocol="SSL",
    ssl_cafile="/home/ka_user001/ssl/key_kafka/ca.crt", # From the connection information for the managed service
    ssl_certfile="/home/ka_user001/ssl/key_kafka/server.crt", # From the connection information for the managed service
    ssl_keyfile="/home/ka_user001/ssl/key_kafka/server.key", # From the connection information for the managed service
    )


# Continuously poll for new messages
for msg in consumer:
  print("Message: ", msg.value)
