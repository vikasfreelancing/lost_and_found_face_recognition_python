from confluent_kafka import Consumer
from initializeFounding import InitializeFounding
conf = {
        'bootstrap.servers': 'moped-01.srvs.cloudkafka.com:9094,moped-02.srvs.cloudkafka.com:9094,moped-03.srvs.cloudkafka.com:9094',
        'group.id': '5h860wrw-consumers', 
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'latest'},
        'security.protocol': 'SASL_SSL',
	    'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': '5h860wrw',
        'sasl.password': 'dJ5Wq7kkovd2V9ROJltMOqhi3K3xS38K'
    }

c = Consumer(**conf)

c.subscribe(['5h860wrw-found_items'])

while True:
    msg = c.poll(0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    print('Received message: {}'.format(msg.value().decode('utf-8')))
    itemId = msg.value().decode('utf-8')
    InitializeFounding().initializeFounding(itemId)

c.close()