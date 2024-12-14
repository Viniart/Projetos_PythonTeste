# FTP - File Transfer Protocol
from ftplib import *

ftp = FTP("ftp.ibge.gov.br")
#ftp = FTP("ftp.ibiblio.org")

print(ftp.getwelcome())

usuario = input("Informe o usuario: ")
senha = input("Informe a senha: ")

ftp.login(usuario, senha)

print("Pasta atual: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()