
#"""
# This is X product
# 
#"""
# 
# Print events inside specified topic

# Run
# print.sh topic_name 
#

TOPIC_NAME=$1
KAFA_DIR="/opt/kafka/"

CONFIG=$2
if [ -z "$CONFIG" ]; then
    echo "use # list.sh client_config_file"
    exit 1
fi


$KAFA_DIR/bin/kafka-topics.sh \
		--delete \
		--topic $TOPIC_NAME \
                --bootstrap-server kafka.kifarunix-demo.com:9092\
                --command-config $CONFIG ;
