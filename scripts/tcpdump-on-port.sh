#!/bin/bash

sudo tcpdump -v -i any port $1 and '(tcp-syn|tcp-ack)!=0'