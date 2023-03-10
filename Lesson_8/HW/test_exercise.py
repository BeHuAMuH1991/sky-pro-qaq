import requests
from pages.Company import Company
from pages.Employee import Employee

company = Company("https://x-clients-be.onrender.com")
employee = Employee("https://x-clients-be.onrender.com")

def test_get_list_employee():
    list_company = company.get_company_list()#Смотрим список компаний
    
    new_company = company.create_company("Engeneer", "Bar")#Создаем новую компанию
    new_list_company = company.get_company_list()#Смотрим обновленный список компаний
    id_company = new_company["id"]#Берем id новой компании
    my_params = {
        "company" : id_company
    }
    lists_employee = employee.list_employee(my_params)
    assert len(new_list_company) - len(list_company) == 1
    assert new_company["id"] == id_company
    assert len(lists_employee) == 0

def test_create_news_employee():
    first_name = "Иван"
    last_name = "Петров"
    middle_name = "Иванович"

    list_company = company.create_company("Барчик", "Закусить и выпить")
    id_company = list_company["id"]
    my_params = {
        "company" : id_company
    }
    new_employee = employee.create_employee(id_company, first_name, last_name, middle_name)
    list_employee = employee.list_employee(my_params)
    assert len(new_employee) == 1
    assert list_employee[0]["firstName"] == first_name
    assert list_employee[0]["lastName"] == last_name
    assert list_employee[0]["middleName"] == middle_name


def test_get_employee_id():

    list_company = company.get_company_list()
    id_company = list_company[0]["id"]
    my_params = {
        "company" : id_company
    }
    lists_employee = employee.list_employee(my_params)
    first_employee = lists_employee[0]["id"]
    _employee = employee.get_employee_id(first_employee)
    assert _employee["companyId"] == id_company
    assert len(_employee) == 11

def test_change_info_employee():
    first_name = "Иван"
    last_name = "Петров"
    middle_name = "Иванович"
    new_info = {
        "lastName": "Ласточкин",
        "email": "235@gmail.com",
        "url": "простой url",
        "isActive": True
    }

    list_company = company.create_company("Барчик", "Закусить и выпить")
    id_company = list_company["id"]
    my_params = {
        "company" : id_company
    }
    new_employee = employee.create_employee(id_company, first_name, last_name, middle_name)

    id_employee = new_employee["id"]
    new_info_employee = employee.change_info_employee(id_employee, new_info)
    assert new_info_employee["email"] == new_info["email"]
    assert new_info_employee["url"]  == new_info["url"]
    assert new_info_employee["id"] == id_employee
    
