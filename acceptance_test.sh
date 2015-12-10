#!/bin/sh
#This scriot must be run as root to work properly

echo Testing to see if dnsmasq is running and listening on port 53

if ps ax | grep -v grep | grep dnsmasq > /dev/null && netstat -tulpn | grep dnsmasq > /dev/null
then
    echo The dnsmasq service is working properly
else
    echo ***Warning the service is not running***
fi
