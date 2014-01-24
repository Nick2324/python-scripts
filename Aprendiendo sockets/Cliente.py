# -*- coding: utf-8 *-*

from SocketServidor import SocketServidor
from SocketCliente import SocketCliente

if __name__ == "__main__":
    numero_clientes = 1  #input("Ingrese el número de clientes: ")
    nombre_dominio = "localhost"  #raw_input("Ingrese el nombre de dominio: ")
    puerto = 3128  #input("Ingrese el puerto: ")
    clientes = []
    servidor = SocketServidor(puerto, nombre_dominio)
    #for i in range(numero_clientes):
    #    clientes.append(SocketCliente())
    #    clientes[i].conectarServidor(puerto, nombre_dominio)
    print servidor.getNombreDominio(), " hola que mas!"
