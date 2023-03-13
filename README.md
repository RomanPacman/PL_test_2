Интструкция по запуску проекта:
1) Создаем проект и выполняем команду pip install Django
2) выполняем команду django-admin startproject 'name_you_app'
3) Делаем всю нужную инсталяцию:
    pip install pandas
    pip install openpyxl xlsxwriter xlrd
    pip install requests
    pip install pydantic
4) Копируем файлы из репозитория с заменой, либо создаем такие-же и копируем код.
5) В папке проекта выполняем команду python manage.py runserver

При переходе по ссылке получаем рабочее приложение (без фронта)

На вход можно передать либо артикул, либо xlms файл с артикулами в первом столбце.
На вывод для удобства чтения передаются данные ответа в табличном виде и сразу же в json-е
Т.к. функция получения данных асинхронна можно делать запроосы по файлу или одному артикулу одновременно
