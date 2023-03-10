from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure



class CompanyTable:
    __scripts = {
        "select": "select * from company",
        "select_only_active":"select * from company where \"isActive\" = true",
        "delete by id": text("delete from company where id = :id_to_delete"),
        "insert new": text("insert into company(\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id": "select MAX(id) from company"

    }
    
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("Удаляем компанию")
    def delete(self, id : int):
        """Удаляем компанию"""
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    @allure.step("Создаем компанию")
    def create(self, name : str, descr : str):
        """Создаем компанию"""
        self.__db.execute(self.__scripts["insert new"], new_name = name, new_descr = descr)
        
    @allure.step("Получаем самый большой id из имеющихся компаний")
    def get_max_id(self) -> int:
        """Получаем самый большой id из имеющихся компаний"""
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]
