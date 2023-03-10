import json


company_json = """
    {
        "id" : 111,
        "isActive" : true,
        "creatDateTime" : "2022-12023T14:43:26.7132",
        "lastChangeDateTime" : "2022-12023T14:43:26.7132",
        "name" : "Барбершоп 'Цирюльник'",
        "discription" : "Крутые стрижки для крутых шишек"
    }"""

def test_parse_json():
    company = json.loads(company_json)
    assert company["id"] == 111