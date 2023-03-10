set result=./result
set rep_history=./allure-report/history
set report=./allure-report
set result_history=\result\history

rmdir /S %result%
pytest --alluredir=%result%
dir C:\Users\Alex\Desktop\Домашка\1Автоматизация\skypro-homeworks\Lesson_9\HW>%result_history%
XCOPY  %rep_history% %result%
rmdir /S %report%
allure generate %result% -o %report%
allure open %report%




