import requests
class API:
    def __init__(self, url:str):
        self.url = url
    def create_key(self):
        req = requests.post(self.url+'/access-keys', verify=False)
        return req
    def get_key(self, id:int):
        req = requests.get(self.url+'/access-keys/'+str(id), verify=False)
        return req