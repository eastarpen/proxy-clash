import protocol.utils as utils
import protocol.constant as constant

class Base():

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name:str):
        self._name = name;

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server:str):
        if not utils.is_server_valid(server):
            raise Exception(f'"{server}"is not a valid server address!')
        self._server = server;

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port:int):
        self._port = port;

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, _type:str):
        if _type not in constant.PROTOCOL_TYPE:
            raise Exception(f'protocol "{_type}" is not supported!')
        self._type = _type

    def __init__(self, server:str, name:str,
            port:int, _type:str) -> None:
        '''
        server: server address
        name: server name
        port: server port
        _type: protocol type
        '''
        self.type = _type
        self.server = server
        self.name = name
        self.port = port
