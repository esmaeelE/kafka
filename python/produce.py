#Producer.py

from kafka import KafkaProducer
import time

# Configuring the Kafka producer 
producer = KafkaProducer(
	bootstrap_servers=f"kafka.kifarunix-demo.com:9092", # From the connection information for the managed service
	    security_protocol="SSL",
	    ssl_cafile="/home/ka_user001/ssl/key_kafka/ca.crt", # From the connection information for the managed service
	    ssl_certfile="/home/ka_user001/ssl/key_kafka/server.crt", # From the connection information for the managed service
	    ssl_keyfile="/home/ka_user001/ssl/key_kafka/server.key", # From the connection information for the managed service
	 )

#message = f"Hello from Python using SSL !"
#producer.send("testssl-topic", message.encode('utf-8'))
#print(f"Message sent: {message}")
#time.sleep(1)
#producer.close()
#

## Generate 10 messages in total with 1 second interval
for i in range(10):
      message = f"Hello from Python using SSL {i + 1}!"
      producer.send("testssl-topic", message.encode('utf-8'))
      print(f"Message sent: {message}")
      time.sleep(1)
producer.close()


