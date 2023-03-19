import requests
import allure

class Company:

    def __init__(self, url):
        self.url = url

    @allure.step("Получаем токен")
    def get_token(self, user : str = 'michaelangelo', password  : str = 'party-dude' ) -> str:
        """Получаем токен после авторизации"""
        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("Получаем список компаний")
    def get_company_list(self, params_to_add : dict = None) -> dict:
        """Получаем список компаний"""
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()
        
    @allure.step("Создаём новую компанию")
    def create_company(self, name : str, description : str = "") -> dict:
        """Создаём новую компанию"""
        company = {
            "name" : name,
            "description" : description
        }
        my_token = {}
        my_token["x-client-token"] = self.get_token()
        res =requests.post(self.url+'/company', json=company, headers=my_token)
        return res.json()