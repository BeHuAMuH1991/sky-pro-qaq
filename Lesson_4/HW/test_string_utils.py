import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

@pytest.mark.parametrize('text, answer', [("skypro", "Skypro"), 
("Skypro", "Skypro"),  
("скайпро", "Скайпро"),
("skypro skypro", "Skypro Skypro"),
("1skypro", "1Skypro"),
("היי.", "היי."),
(" skypro", " Skypro"),
(" skypro", "Skypro")
])
def test_capital_letter(text, answer):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(text)
    assert res == answer

@pytest.mark.parametrize('text, answer', [(" skypro", "skypro"),
 ("  skypro", "skypro"),
  ("skypro", "skypro"),
  (" skypro    ", "skypro    "),
  ("    skypro    ","skypro    ")])
def test_whitespace(text, answer):
    stringUtils = StringUtils()
    res = stringUtils.trim(text)
    assert res == answer

@pytest.mark.parametrize('text, deli, answer', [("Привет,Мир", "," , ["Привет",  "Мир"]),
 ("Привет!Мир", "!", ["Привет", "Мир"]),
  ("Привет Мир", "!", ["Привет Мир"]),
  ("Привет Мир", " ", ["Привет", "Мир"]),
  ("Привет.Мир.Меня.Зовут.Алексей", ".", ["Привет", "Мир", "Меня", "Зовут", "Алексей"])])
def test_splitting_lines(text, deli, answer):
    stringUtils = StringUtils()
    res = stringUtils.to_list(text, deli)
    assert res == answer

def test_splitting_lines():
    stringUtils = StringUtils()
    res = stringUtils.to_list("Привет,Мир,Меня,Зовут,Алексей")
    assert res == ["Привет", "Мир", "Меня", "Зовут", "Алексей"]

@pytest.mark.parametrize('text, sumbol, answer', [("Skypro", "S", True), ("Skypro", "s", False), ("Скайпро", "С", True), ("Skypro", "", True)])
def test_search(text, sumbol, answer):
    stringUtils = StringUtils()
    c = stringUtils.contains(text, sumbol)
    assert c == answer 

@pytest.mark.parametrize('text, sumbol, answer', [("SkyPro", "Sky", "Pro"), 
("SkyPro", "sky", "SkyPro"), 
("SkyPro", "asfdsgf", "SkyPro"),
("", "", ""),
(" ", " ", ""),
("SkyPro", "yPr", "Sko"),])
def test_deli(text, sumbol, answer):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(text, sumbol)
    assert res == answer    

@pytest.mark.parametrize('text, sumbol, answer', [("SkyPro", "S", True),
 ("SkyPro", "k", False),
  ("SkyPro", "", True),
  ("SkyPro", "Sky", True),
  (" SkyPro", " ", True)])
def test_start(text, sumbol, answer):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(text, sumbol)
    assert res == answer

@pytest.mark.parametrize('text, sumbol, answer', [("SkyPro", "o", True),
 ("SkyPro", "k", False),
  ("SkyPro", "", True),
  ("SkyPro ", " ", True)])
def test_start(text, sumbol, answer):
    stringUtils = StringUtils()
    res = stringUtils.end_with(text, sumbol)
    assert res == answer


@pytest.mark.parametrize('text, answer', [("", True),
 ("SkyPro", False),
 ("    ", True),
  ("         SkyPro", False),
  ("Sky Pro Sky Pro", False),
  (" Sky Pro Sky Pro ", False),
  ("        Sky Pro Sky Pro         ", False)])
def test_start(text, answer):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(text)
    assert res == answer

@pytest.mark.parametrize('list1, deli, answer', [([1,2,3,4,5,6], "-", "1, 2, 3, 4, 5, 6"),
 (["Sky", "Pro"], " ", "Sky Pro"),
  (["Sky", "Pro"], "", "SkyPro"),
  ([], "-", ""),
  ])
def test_bind(list1, deli, answer):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list1, deli)
    assert res == answer

def test_bind():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(["Привет", "Мир!", "Как", "у тебя", "дела?"])
    assert res == "Привет,Мир!,Как,у тебя,дела?"

def test_bind():
    stringUtils = StringUtils()
    res = stringUtils.list_to_string([1], "-")
    assert res == "1"



