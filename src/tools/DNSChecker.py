from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP

def dns_analyzer(packet):
    if packet.haslayer(DNS):
        # Vérifier si c'est une requête DNS
        if packet.haslayer(DNSQR):
            dns_query = packet[DNSQR].qname.decode('utf-8')
            print(f"[+] DNS : {dns_query}")

        # Vérifier si c'est une réponse DNS
        if packet.haslayer(DNSRR):
            dns_response = packet[DNSRR].rdata
            print(f"[+] DNS ANSWERS : {dns_response}")

            if isinstance(dns_response, str) and dns_response.startswith(("10.", "172.16.", "192.168.")):
                print(f"[!] Wierd DNS : {dns_response}")

def start_dns_sniffing(interface=None):
    print("[*] Starting ...")
    if interface:
        sniff(iface=interface, filter="udp port 53", prn=dns_analyzer, store=0)
    else:
        sniff(filter="udp port 53", prn=dns_analyzer, store=0)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ANALYZER")
    parser.add_argument("-i", "--interface", help="")
    args = parser.parse_args()
    start_dns_sniffing(interface=args.interface)