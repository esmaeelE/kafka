# kcat
 
kcat is a CLI for kafka and work as kafka client.

Think of it as a netcat for Kafka

* [Kcat](https://github.com/edenhill/kcat)

```
$ sudo apt install kafkacat
```

### List topics

```
kafkacat -L -b localhost:9094
```

### Print messages inside a specific topic

* Read 

```
kafkacat -b 172.16.5.85:9092 -C -t test_topic
```

```
kafkacat -L -b 172.16.5.85:9092 -o earliest -t first.messages
```


