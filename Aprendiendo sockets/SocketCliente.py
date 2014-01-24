# -*- coding: utf-8 *-*

from socket import socket
from Socket import Socket


class SocketCliente(Socket):

    _socketC = None

    def __init__(self):
        self._socketC = socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectarServidor(self, puerto, nombre_dominio=""):
        self._socketC.connect((nombre_dominio, puerto))

    def enviarMensaje(self, mensaje):
        self._socketC.send(mensaje)

    def cerrarConexion(self):
        self._socketC.close()
