# ARP Spoofing Simulation

This project simulates an ARP spoofing attack to illustrate how vulnerabilities in the ARP protocol can be exploited in network environments. It provides hands-on experience with network analysis tools and explores security countermeasures.

## Overview

ARP spoofing, also known as ARP cache poisoning, is a technique where an attacker sends false ARP (Address Resolution Protocol) messages to a target device on a local network. By associating the attacker's MAC address with the IP address of a legitimate gateway, the attacker can intercept, monitor, or modify data transmitted across the network.

### Features
- Demonstrates ARP spoofing with Python using Scapy
- Monitors network traffic with Wireshark for analysis
- Explores countermeasures such as static ARP entries and Dynamic ARP Inspection (DAI)

## Getting Started

### Prerequisites
- Python 3.x
- Scapy library (`pip install scapy`)
- Wireshark (optional for traffic analysis)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/arp-spoofing-simulation.git
   cd arp-spoofing-simulation
