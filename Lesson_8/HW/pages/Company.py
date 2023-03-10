import requests

class Company:

    def __init__(self, url):
        self.url = url

    def get_token(self, user = 'michaelangelo', password = 'party-dude' ):#Получаем токен

        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    def get_company_list(self, params_to_add= None):#Получаем список компаний
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()

    def create_company(self, name, description = ""):#Создание новой компании
        company = {
            "name" : name,
            "description" : description
        }
        my_token = {}
        my_token["x-client-token"] = self.get_token()
        res =requests.post(self.url+'/company', json=company, headers=my_token)
        return res.json()