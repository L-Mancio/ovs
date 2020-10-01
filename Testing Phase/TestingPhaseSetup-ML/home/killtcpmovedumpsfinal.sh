#!/bin/bash
read -p "enter website name: " site
read -p "enter webpage name: " page

pkill tcpdump
mv s31$site.pcap s32$site.pcap /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/$site-pcaps/$page/

mergecap -F pcap -w  /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/$site-pcaps/$page/$site$page.pcap /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/$site-pcaps/$page/s31$site.pcap /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/$site-pcaps/$page/s32$site.pcap

cp /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/$site-pcaps/$page/$site$page.pcap /media/sf_VMshared/Testing\ Scripts/pcaps-aggr5/pcap-waggr5/