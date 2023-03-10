from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure



class EmployeeTable:


    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    @allure.step("Ищем сотрудников по id компании")
    def get_employee(self, id: int) -> dict:
        """Ищем сотрудников по id компании"""

        return self.__db.execute(text("select * from  employee  where \"companyId\" = :company_id"), company_id = id).fetchall()


    @allure.step("Создаем сотрудника в компании по id компании")
    def create_employee(self, first_name: str, last_name: str, phone: str, id: int):
        """Создаем сотрудника в компании по id компании"""
        self.__db.execute(text("insert into  employee (\"first_name\", \"last_name\", \"phone\" , \"companyId\") values (:first_name_, :last_name_, :phone_, :id_company)"), first_name_ = first_name, last_name_ = last_name, phone_ = phone, id_company = id)


    @allure.step("Удаляем сотрудника по id сотрудника")
    def delete_employee(self, id: int): 
        """Удаляем сотрудника по id сотрудника"""

        self.__db.execute(text("delete from employee  where \"id\" = :id_employee"), id_employee = id)

    @allure.step("Поиск сотрудника по id сотрудника")
    def search_one_employee(self, id: int) -> dict: 
        """Поиск сотрудника по id сотрудника"""

        return self.__db.execute(text("select * from  employee  where \"id\" = :employee_id"), employee_id = id).fetchall()

    @allure.step("Изменяем информацию о сотруднике")
    def update_employee(self, new_first_name: str, new_last_name: str, id: int, new_phone: str = None):
        """Изменяем информацию о сотруднике"""
        self.__db.execute(text("update employee set \"first_name\"  = :first_name, \"last_name\" = :last_name, \"phone\" = :phone WHERE id = :id"), first_name = new_first_name, last_name = new_last_name, phone = new_phone, id = id)
