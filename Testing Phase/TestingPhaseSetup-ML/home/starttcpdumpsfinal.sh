#!/bin/bash
read -p "enter website name: " site

tcpdump -i s3-eth1 -w s31$site.pcap port not 53 &

tcpdump -i s3-eth2 -w s32$site.pcap port not 53 &
