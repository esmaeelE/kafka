
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


$KAFA_DIR/bin/kafka-topics.sh \
		--delete \
		--topic $TOPIC_NAME \
		--bootstrap-server localhost:9094 ;
