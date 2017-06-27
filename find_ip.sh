#!/bin/bash
echo "WiFi  "`ifconfig wlan | grep -Eo "inet addr:(([0-9]{1,3}.){3}[0-9].{1,3})"`
echo "Wired "`ifconfig eth0 | grep -Eo "inet addr:(([0-9]{1,3}.){3}[0-9].{1,3})"`

