import requests
import allure
from pages.Company import Company



class Employee:
    company = Company("https://x-clients-be.onrender.com")

    def __init__(self, url):
        self.url = url

    @allure.step("Получаем список сотрудников по id компании")
    def list_employee(self, paramparams_to_add : dict= None) -> dict:
        """Получаем список сотрудников по id компании"""
        lists = requests.get(self.url+"/employee", params= paramparams_to_add)
        return lists.json()


    @allure.step("Получиаем информацию о сотруднике по его id")
    def get_employee_id(self, id : int) -> dict:
        """Получаем информацию о сотруднике по его id"""
        employee = requests.get(self.url+"/employee/"+str(id))
        return employee.json()



