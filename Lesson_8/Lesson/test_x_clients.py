import requests
from CompanyApi import CompanyApi





api = CompanyApi("https://x-clients-be.onrender.com")

def test_get_companies():#Список всех компаний
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():#Список активных компаний
    #Получаем список всех компаний
    full_list = api.get_company_list()
    #Получаем список активных компаний
    activ_list = api.get_company_list(params_to_add={'activ' : 'true'})

    assert len(full_list) == len(activ_list)

def test_add_new_company():
    #Получить количество компаний до создания компаний
    body = api.get_company_list()
    len_before = len(body) 

    #Создать новую
    name  = "Autotest"
    descr = "Dhjnkmsd"
    result = api.create_company(name, descr)
    new_id = result["id"]

    #Получить количество компаний
    body = api.get_company_list()
    len_after = len(body)

    #Проерить что компаний +1
    assert len_after - len_before == 1
    #Проверить что id последней компании равно шагу номер 2
    #Проверить название и описание последней компании
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id

def test_get_one_company():
    name = "VS Code"
    descr  = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr

def test_edit():
    new_id = api.create_edit("Companyto be edited", "Edit me")

    new_name = "UPDATE"
    new_descr = "__upd__"
    edited = api.edit(new_id, new_name, new_descr)

    assert edited["id"] == new_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr