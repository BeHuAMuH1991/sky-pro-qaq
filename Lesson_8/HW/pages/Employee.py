import requests
from pages.Company import Company


class Employee:
    company = Company("https://x-clients-be.onrender.com")

    def __init__(self, url):
        self.url = url

    def list_employee(self, paramparams_to_add= None):#Получить список сотрудников по id компании
        lists = requests.get(self.url+"/employee", params= paramparams_to_add)
        return lists.json()

#Создать нового сотрудника
    def create_employee(self, id_company, first_name, last_name, middle_name, phone = "+7...", url = ""):
        dictionary_new_employee = {
            "companyId": id_company,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "phone": phone,
            "url": url
        }
        company = Company(self.url)
        my_token = {}
        my_token["x-client-token"] = company.get_token()
        new_employee = requests.post(self.url+"/employee", json=dictionary_new_employee, headers=my_token)
        return new_employee.json()

    def get_employee_id(self, id):
        employee = requests.get(self.url+"/employee/"+str(id))
        return employee.json()

    def change_info_employee(self, id, info):
        company = Company(self.url)
        my_token = {}
        my_token["x-client-token"] = company.get_token()

        change_info = requests.patch(self.url+"/employee/"+str(id), json=info, headers=my_token)
        return change_info.json()
