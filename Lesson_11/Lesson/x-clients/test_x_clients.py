import requests
from CompanyApi import CompanyApi

def test_get_companies(client: CompanyApi):#Список всех компаний
    body = client.get_company_list()
    assert len(body) > 0

def test_get_active_companies(client: CompanyApi):#Список активных компаний
    #Получаем список всех компаний
    full_list = client.get_company_list()
    #Получаем список активных компаний
    activ_list = client.get_company_list(params_to_add={'activ' : 'true'})

    assert len(full_list) == len(activ_list)

def test_add_new_company(client: CompanyApi):
    #Получить количество компаний до создания компаний
    body = client.get_company_list()
    len_before = len(body) 

    #Создать новую
    name  = "Autotest"
    descr = "Dhjnkmsd"
    result = client.create_company(name, descr)
    new_id = result["id"]

    #Получить количество компаний
    body = client.get_company_list()
    len_after = len(body)


    #Проверить что id последней компании равно шагу номер 2
    #Проверить название и описание последней компании
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id

def test_get_one_company(client: CompanyApi):
    name = "VS Code"
    descr  = "IDE"
    result = client.create_company(name, descr)
    new_id = result["id"]

    new_company = client.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr

def test_edit(client: CompanyApi):
    new_id = client.create_edit("Companyto be edited", "Edit me")

    new_name = "UPDATE"
    new_descr = "__upd__"
    edited = client.edit(new_id, new_name, new_descr)

    assert edited["id"] == new_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr