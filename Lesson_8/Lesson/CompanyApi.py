import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url

    
    def get_company_list(self, params_to_add= None):#Получакм список компаний
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()

    def get_token(self, user = 'michaelangelo', password = 'party-dude' ):#Получаем токен

        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description = ""):#Создание новой компании
        company = {
            "name" : name,
            "description" : description
        }
        my_token = {}
        my_token["x-client-token"] = self.get_token()
        res =requests.post(self.url+'/company', json=company, headers=my_token)
        return res.json()

    def get_company(self, id):#Поиск компании по id получаем json
        resp = requests.get(self.url+'/company/'+str(id))
        return resp.json()

    def create_edit(self, name, description = ""):#Создание новой компании и получаем id
        company = {
            "name" : name,
            "description" : description
        }
        my_token = {}
        my_token["x-client-token"] = self.get_token()
        res =requests.post(self.url+'/company', json=company, headers=my_token).json()
        return res["id"]

    def edit(self, new_id, new_name, new_descr):
        my_token = {}
        my_token["x-client-token"] = self.get_token()
        company = {
            "name" : new_name,
            "description" : new_descr
        }
        resp = requests.patch(self.url+'/company/'+str(new_id), headers=my_token, json=company)
        return resp.json()

