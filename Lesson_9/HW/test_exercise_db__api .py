import allure
from pages.CompanyTable import CompanyTable
from pages.EmployeeTable import EmployeeTable
from pages.Company import Company
from pages.Employee import Employee




api_employee = Employee("https://x-clients-be.onrender.com")
api_company = Company("https://x-clients-be.onrender.com")
db_company = CompanyTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")
db_employee = EmployeeTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")

@allure.feature("Поиск")
@allure.title("Получаем список сотрудников в новой компании")
@allure.epic("Сотрудник")
def test_get_list_employee():
    list_company = api_company.get_company_list()#Смотрим список компаний
    db_company.create("Беги Форест", "Быстро бегаешьстолько же пьешь")#Создаем новую компанию
    new_list_company = api_company.get_company_list()#Смотрим обновленный список компаний
    id_company = db_company.get_max_id()#Берем id новой компании
    params = {
        "company" : id_company
    }
    list_employee_new_company = api_employee.list_employee(params)
    db_company.delete(id_company)

    assert len(new_list_company) - len(list_company) == 1
    assert len(list_employee_new_company) == 0

@allure.feature("Создание")
@allure.title("Создание нового сотрудника")
@allure.epic("Сотрудник")
def test_create_news_employee():
    first_name = "Иван"
    last_name = "Петров"
    phone = "8922333654"

    db_company.create("Барчик", "Закусить и выпить")
    id_company = db_company.get_max_id()

    db_employee.create_employee(first_name, last_name, phone, id_company)

    list_employee = db_employee.get_employee(id_company)
    db_id_employee = list_employee[0][0]
    db_employee.delete_employee(db_id_employee)
    db_company.delete(id_company)


    assert list_employee[0][4] == first_name
    assert list_employee[0][5] == last_name
    assert list_employee[0][7] == phone

@allure.feature("Поиск")
@allure.feature("Изменение информации")
@allure.title("получение информации по id сотрдника")
@allure.epic("Сотрудник")
def test_get_employee_id():
    first_name = "Петр"
    last_name = "Петров"
    phone = "8922333654"

    list_company = api_company.get_company_list()
    id_company = list_company[0]["id"]
    db_employee.create_employee(first_name, last_name, phone, id_company)
    my_params = {
    "   company" : id_company
    }

    list_employee = api_employee.list_employee(my_params)
    api_id_employee = list_employee[-1]["id"]
    one_employee = api_employee.get_employee_id(api_id_employee)
    
    db_employee.delete_employee(api_id_employee)

    assert one_employee["firstName"] == first_name
    assert one_employee["lastName"] == last_name
    assert one_employee["phone"] == phone


@allure.feature("Изменение информации")
@allure.title("Изменение информации о сотруднике")
@allure.epic("Сотрудник")
def test_change_info_employee():
    first_name = "Иван"
    last_name = "Петров"
    middle_name = "Иванович"
    new_first_name = "Петр"
    new_last_name = "Иванов"
    new_phone = "нет телефона"

    db_company.create("Барчик", "Закусить и выпить")
    id_company = db_company.get_max_id()

    db_employee.create_employee(first_name, last_name, middle_name, id_company)
    my_params = {
        "company" : id_company
    }

    list_employee = api_employee.list_employee(my_params)
    api_id_employee = list_employee[-1]["id"]
    db_employee.update_employee(new_first_name, new_last_name, api_id_employee, new_phone)
    new_info_employee = api_employee.get_employee_id(api_id_employee)
    db_employee.delete_employee(api_id_employee)
    db_company.delete(id_company)
    
    assert new_info_employee["firstName"] == new_first_name
    assert new_info_employee["lastName"] == new_last_name
    assert new_info_employee["phone"] == new_phone

