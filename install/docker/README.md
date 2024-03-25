# Run simple kafka server with UI

Based on KAFKA UI with little modification

* [Kafka UI codes](https://github.com/provectus/kafka-ui/tree/master/documentation/compose)

Use server IP instead of localhost in **KAFKA_ADVERTISED_LISTENERS** environments.
```
KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT://kafka1:29092,PLAINTEXT_HOST://172.16.5.85:9092'
```

## Run

### Start 
```
docker-compose -f kafka-ui.yaml up -d
```
### Stop and Remove

```
docker-compose -f kafka-ui.yaml down -v
```


#### 

If only use these container can prune to remove all of them

```
docker container prune
docker volume prune
```
