import re

from protocol.Base import Base

# TODO
# add name

class SS(Base):

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, method:str):
        self._method = method

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password:str):
        self._password = password

    def __init__(self, link:str) -> None:
        super().__init__('ss')
        params = self.get_params(link)
        self.password = params['password']
        self.method = params['method']
        self.name = 'test'
        self.server = params['server']
        self.port = params['port']

    def get_params(self, link:str) -> dict:
        params = self.bs64_decode(link)
        print(params)
        res = re.match(r'(.*?):(.*?)@(.*?):(\d+)', params)
        if None == res:
            raise Exception(f'"{link}" is not a valid link')
        return {
            'method': res.group(1),
            'password': res.group(2),
            'server': res.group(3),
            'port': res.group(4),
        } 
