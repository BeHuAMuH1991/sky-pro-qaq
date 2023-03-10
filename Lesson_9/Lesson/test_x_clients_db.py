import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


db = CompanyTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")

api = CompanyApi("https://x-clients-be.onrender.com")


@allure.id("SkyPro1")
@allure.story("Получение списка компаний")
@allure.epic("Компания")
@allure.feature("REad")
@allure.title("Получение списка организации")
def test_get_companies():#Список всех компаний
    #Получить список через APi
    api_result = api.get_company_list()
    # Получить список из БД
    db_result = db.get_comnaies()
    # Проверить что списки равны
    assert len(api_result) != len(db_result)

@allure.id("SkyPro2")
@allure.epic("Компания")
@allure.feature("REad1")
@allure.title("Получение списка активных организации")
def test_get_active_companies():#Список активных компаний
    #Получаем список всех компаний
    #Получаем список активных компаний
    activ_list = api.get_company_list(params_to_add={'activ' : 'true'})
    db_list = db.get_activ_companies()
    assert len(activ_list) != len(db_list)

@allure.id("SkyPro3")
@allure.epic("Компания")
@allure.feature("Create")
@allure.title("Создание компании")
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

    db.delete(new_id)

    #Проерить что компаний +1
    assert len_after - len_before == 1
    #Проверить что id последней компании равно шагу номер 2
    #Проверить название и описание последней компании
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id


@allure.id("SkyPro4")
@allure.epic("Компания")
@allure.feature("REad")
@allure.title("Поиск компании по id")
def test_get_one_company():
    name = 'SkyPro'
    descr = 'Онлайн'
    db.create(name, descr)
    max_id = db.get_max_id()
    new_company = api.get_company(max_id)
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name

@allure.id("SkyPro5")
def test_edit():
    new_id = api.create_edit("Companyto be edited", "Edit me")

    new_name = "UPDATE"
    new_descr = "__upd__"
    edited = api.edit(new_id, new_name, new_descr)

    assert edited["id"] == new_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr