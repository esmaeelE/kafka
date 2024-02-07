
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
echo $TOPIC_NAME

CONFIG=$2
if [ -z "$CONFIG" ]; then
    echo "use # list.sh client_config_file"
    exit 1
fi

# echo $TOPIC_NAME, $CONFIG

$KAFA_DIR/bin/kafka-console-consumer.sh \
			--topic $TOPIC_NAME \
			--from-beginning \
			--bootstrap-server kafka.kifarunix-demo.com:9092 \
			--property print.key=true \
			--consumer.config $CONFIG \
			--property key.separator=" : ";


