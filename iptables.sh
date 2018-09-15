#!/bin/bash

# simple script to get up and running with a basic stateful firewall on Arch Linux distros

# install iptables
	#pacman -S iptables

# check rules
	#iptables-save
	#iptables -nvL --line-numbers

# clear all rules
	iptables-restore < /etc/iptables/empty.rules
	sleep 1

# create 2chainz
	iptables -N TCP
	iptables -N UDP

# this script is not for a NAT gateway
	iptables -P FORWARD DROP

# allow loopback traffic
	iptables -A INPUT -i lo -j ACCEPT
	iptables -A OUTPUT -o lo -j ACCEPT
	#alternatively
		#iptables -A INPUT -s 127.0.0.1 -j ACCEPT
		#^INPUT^OUTPUT

# sake of simplicity allow outbound
	iptables -P OUTPUT ACCEPT

# input policy will stay accept incase rules are flushed
	iptables -P INPUT ACCEPT
	iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
	#iptables -A INPUT -p 41 -j ACCEPT #uncomment for icmpv6 neighbor discovery
	iptables -A INPUT -m conntrack --ctstate INVALID -j DROP
	iptables -A INPUT -p icmp --icmp-type 8 -m conntrack --ctstate NEW -j ACCEPT
	iptables -A INPUT -p udp -m conntrack --ctstate NEW -j UDP
	iptables -A INPUT -p tcp --syn -m conntrack --ctstate NEW -j TCP
	iptables -A UDP -p udp -j REJECT --reject-with icmp-port-unreachable
	iptables -A TCP -p tcp -j REJECT --reject-with tcp-reset
	iptables -A INPUT -j REJECT --reject-with icmp-proto-unreachable

