import scapy.all as scapy
from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=processar_pacote)

def processar_pacote(pacote):
    # Verifico se o pacote é HTTP
    if pacote.haslayer(http.HTTPRequest):
        print(pacote)

sniffing('Ethernet')