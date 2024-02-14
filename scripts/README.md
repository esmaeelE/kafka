# Some helper script to communicate kafka server

## Is kafka Runnig

```
$ systemctl is-active kafka.service
```

## List all topics on runing kafka instance

```
$ bash list_topic.sh
$ bash ssl_list_topic.sh ssl_config.properties
```

## Create topic on kafka instance

```
$ bash create_topic.sh topicname
$ bash ssl_list_topic.sh config_ssl.properties
```

## Delete topic

```
$ bash ssl_delete_topic.sh quickstart-events config_ssl.properties
$ bash delete_topic.sh helloworld
```


