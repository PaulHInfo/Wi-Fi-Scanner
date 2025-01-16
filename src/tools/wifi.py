from scapy.all import *
import scapy.all as scapy


def scan():
    request = scapy.ARP()
    request.pdst = conf.route.route("0.0.0.0")[2]+'/24'
    print("Votre IP : " + conf.route.route("0.0.0.0")[1])
    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]
    for element in clients:
        #print(element)
        print(element[1].psrc + "	 " + element[1].hwsrc)

def discover_wifi():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    decoded_devices = devices.decode('utf-8')
    print(decoded_devices)



