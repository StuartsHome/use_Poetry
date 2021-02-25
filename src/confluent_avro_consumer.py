import os
from confluent_kafka.avro import AvroConsumer

TOPIC = "TBD"

def consume_message():
    default_group_name = "default-consumer-group"

    consumer_config = {
        "ssl.endpoint.identification.algorithm" : "https",
        "bootstrap.servers" : "TBD",
        "security.protocol" :"SASL_SSL",
        "sasl.jaas.config" : "TBD"
        "password='{}'".format(
            os.environ["KAFKA_API_KEY"], os.environ["KAFKA_API_SECRET"]
        ),
        "sasl.mechanism": "PLAIN",
        "request.timeout.ms": 1000,
        "group.id": default_group_name,
        "auto.offset.reset": "earliest",
    }

    consumer = AvroConsumer(consumer_config)
    consumer.subscribe(TOPIC)

    try:
        message = consumer.poll(5)
    except Exception as e:
        print(f"exception while trying to poll messages - {e}")
    else:
        if message:
            print(
                f"successfully received a record from "
                f"Kafka topic: {message.topic()}, partition: {message.partition()}, offset: {message.offset()}\n"
                f"message key: {message.key()} || message value: {message.value()}"
            )
            consumer.commit()
        else:
            print("No new messages at this point. Try again later.")
    consumer.close()