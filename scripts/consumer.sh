
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

$KAFA_DIR/bin/kafka-console-consumer.sh \
			--topic $TOPIC_NAME \
			--from-beginning \
			--bootstrap-server localhost:9094 \
			--property print.key=true \
			--property key.separator=" : ";

