# Run simple kafka server with UI

Based on KAFKA UI with little modification

* [Kafka UI codes](https://github.com/provectus/kafka-ui/tree/master/documentation/compose)


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
