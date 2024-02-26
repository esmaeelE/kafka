# kafka
About kafka


# Run with kraft config

Append my `server.properties` configs to `config/kraft/server.properties` 
Then run server with this command 

```
$ bin/kafka-server-start.sh config/kraft/server.properties
```

# Administration

Kafkacator kcat is a CLI for kafka and work as kafka client.

* [Kcat](https://github.com/edenhill/kcat)

```
$ sudo apt install kafkacat
```

### List topics

```
kafkacat -L -b localhost:9094
```
