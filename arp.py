from scapy.all import ARP, Ether, srp

# Target IP address
target_ip = "192.168.1.1"

# Create an ARP request packet
arp_request = ARP(pdst=target_ip)

# Create an Ethernet frame
ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast MAC address

# Combine Ethernet frame and ARP request
packet = ether / arp_request

# Send the packet and receive the response
result = srp(packet, timeout=3, verbose=False)[0]

# Process the response
for sent, received in result:
    print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
