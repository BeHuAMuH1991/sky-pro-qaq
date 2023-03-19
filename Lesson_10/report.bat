set result=.\result
set rep_history=.\allure-report\history*
set report=.\allure-report


rd /s /q "%result%"
pytest --alluredir="%result%"
allure generate "%result%" -o "%report%"
allure open allure-report
mv "%rep_history%" "%result%"
rd /s /q "%report%"