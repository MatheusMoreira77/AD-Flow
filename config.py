#
#=========================================
#AD-Flow - Automação Active Directory
#Desenvolvido por: Matheus Santos Moreira
#Data: 11/08/2025
#Contato: https://www.linkedin.com/in/matheus-santos-moreira-0a0812261/
#Versão: 1.0
#Descrição: Script para automação de criação e gerenciamento de usuários no Active Directory via terminal.
#=========================================
#

from ldap3 import Server, Connection, ALL

def Conexao_AD():
    server = Server()
    conn = Connection(server, auto_bind=True)

    if not conn.bind():
        print("Erro ao conectar ao servidor LDAP.")
    else:
        print("Conexão estabelecida com sucesso.")