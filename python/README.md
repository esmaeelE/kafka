# How to communicate with kafka server with python clinet

## Prerequisites

```
$ sudo apt install python3-kafka

Or Using pip

$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install kafka-python
```

## Run

* Producer

```
python3 producer.py 
```

Arguments order
	 topic key value

* Consumer 

```
python3 consumer.py 
```
