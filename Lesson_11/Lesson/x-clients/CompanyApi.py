import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url
        self.headers = {"x-client-token" : self.get_token()}

    def get_token(self, user = 'michaelangelo', password = 'party-dude' ):#Получаем токен

        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    
    def get_company_list(self, params_to_add= None):#Получакм список компаний
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()



    def create_company(self, name, description = ""):#Создание новой компании
        company = {
            "name" : name,
            "description" : description
        }

        res = requests.post(self.url+'/company', json=company, headers=self.headers)
        return res.json()
        x =1

    def get_company(self, id):#Поиск компании по id получаем json
        resp = requests.get(self.url+'/company/'+str(id))
        return resp.json()

    def create_edit(self, name, description = ""):#Создание новой компании и получаем id
        company = {
            "name" : name,
            "description" : description
        }

        res =requests.post(self.url+'/company', json=company, headers=self.headers).json()
        return res["id"]

    def edit(self, new_id, new_name, new_descr):
        company = {
            "name" : new_name,
            "description" : new_descr
        }
        resp = requests.patch(self.url+'/company/'+str(new_id), headers=self.headers, json=company)
        return resp.json()

