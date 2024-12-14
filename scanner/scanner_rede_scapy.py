import scapy.all as scapy

def escanear_rede(endereco):
    scapy.arping(endereco)

escanear_rede("172.16.5.215/24")