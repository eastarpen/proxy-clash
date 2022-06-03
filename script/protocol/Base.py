import re
import base64

PROTOCOL_TYPE = ['ssr', 'ss', 'vmess', 'trojan']

def is_server_valid(server:str) -> bool:
    '''
    check whether the server address is valid
    ipv4 address and domain are applied
    '''
    domainPattern = r'\b((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}\b'
    ipv4Pattern = r'^(((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4})$'
    return None != re.match(domainPattern, server) or None != re.match(ipv4Pattern, server)

    
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
        if not is_server_valid(server):
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
        if _type not in PROTOCOL_TYPE:
            raise Exception(f'protocol "{_type}" is not supported!')
        self._type = _type

    def bs64_decode(self, content:str) -> str:
        content = content.replace('-', '+')
        content = content.replace('_', '/')
        return base64.b64decode(content.encode()).decode()

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
