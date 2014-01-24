# -*- coding: utf-8 *-*

from collections import deque
from socket import socket
from Socket import Socket


class SocketServidor(Socket):

    _socketS = None
    _colaSocketC = None
    _ejecutadorPeticion = None

    def __init__(self, puerto, nombre_dominio=""):
        self._socketS = socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socketS.bind((nombre_dominio, puerto))
        self._colaSocketC = deque([])

    def escuchar(self, numeroConexiones):
        self._socketS.listen(numeroConexiones)

    def ejecutarPeticion(self):
        if len(self._colaSocketC) != 0:
            socketCliente = self._colaSocketC.popleft()
            self.terminarConexion(socketCliente)

    def aceptarConexion(self):
        self._colaSocketC.append(self._socketS.accept())

    def terminarConexion(self, socketTerminado):
        socketTerminado.close()

    def terminarServidor(self):
        self._socketS.close()

    def setNombreDominio(self):
        pass

    def setPuerto(self):
        pass

    def getNombreDominio(self):
        return self._socketS.gethostname()

    def getPuerto(self):
        pass
