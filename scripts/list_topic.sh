
#"""
# This is X product
# 
#"""
# 
# List topics inside kafak server

# Run
# list.sh client_config_file
# example 
# bash list.sh kafka-client-ssl-test.properties
#

KAFA_DIR="/opt/kafka/"

$KAFA_DIR/bin/kafka-topics.sh \
		--list \
		--bootstrap-server kafka.kifarunix-demo.com:9094;

