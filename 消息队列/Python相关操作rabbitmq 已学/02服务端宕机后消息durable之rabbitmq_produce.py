#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 16:18
# @Author  : liuhu
# @Site    :
# @File    : 02服务端宕机后消息durable之rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.37.134'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='durable_queue_name', durable=True)

channel.basic_publish(exchange='',
                      routing_key='durable_queue_name',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
