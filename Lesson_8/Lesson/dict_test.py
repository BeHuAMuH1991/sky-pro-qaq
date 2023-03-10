import pytest

empty_dict = {
    
}

footbal_stats = {
    "Число стран" : 48,
    "Страна где проходило" : "Катар",
    "Участники" : ["Австралия", "Англия", "Аргентина", "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды" : {
        "Золотой мяч" : "Лионель Месси",
        "Серебряный мяч" : "Киллиан Мбаппе",
        "Золотая бутса" : "Киллиан Мбаппе",
        "Серебряная бутса" : "Киллиан Мбаппе",
        "Больше всего голов" : {
        "Игрок" : "Киллиан Мбаппе - капитан команды",
        "Количество мячей" : 8
    },
    }
}


def test_empty_dict():
    assert len(empty_dict) == 0

def test_read_value():
    count = footbal_stats.get("Число стран")
    assert count == 48

def test_read_value_():
    country = footbal_stats["Страна где проходило"]
    assert country == "Катар"

def test_write_value():
    footbal_stats["Число стран"] = 50
    count = footbal_stats.get("Число стран")
    assert count == 50

def test_new_value():
    len_before = len(footbal_stats)
    footbal_stats["Победитель"] = "Аргентина"
    winner = footbal_stats.get("Победитель")
    assert winner == "Аргентина"
    assert len(footbal_stats) == len_before + 1


def test_read_list():
    participants = footbal_stats["Участники"]
    england = participants[1]


    assert len(participants) > 0
    assert participants[0] =="Австралия"
    assert england == "Англия"

def test_read_dict():
    total_gols = footbal_stats["Награды"]["Больше всего голов"]["Количество мячей"]
    assert total_gols == 8

def test_save_dict():

    awards = footbal_stats["Награды"]
    player = awards["Больше всего голов"]["Игрок"]
    assert player == "Киллиан Мбаппе - капитан команды"

def test_read_error():
    with pytest.raises(KeyError):
        value = empty_dict["key"]
    
def test_get_empty_or_default():
    value = empty_dict.get("key", "abc123")
    assert value == "abc123"