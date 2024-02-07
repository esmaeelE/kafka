/etc/systemd/system/kafka.service


[Unit]
Description=Apache Kafka
Requires=network.target
After=network.target

[Service]
Type=simple
ExecStart=/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/kraft/server.properties
ExecStop=/opt/kafka/bin/kafka-server-stop.sh
Restart=on-failure

sudo systemd daemon-reload

not enable yet for test purpose  


sudo systemd enable kafka.service

logs
journalctl -f -u kafka


