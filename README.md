# ASCII_passwork_framework


**установка:**
	
> bash/shell:
```
		python3 -m venv venv && \
		source venv/bin/activate && \
		pip install -U pip && \
		pip install -Ur requirements.txt
```


- 	хост - http://172.17.128.22/api/v4
- 	dependencies - python 3.9
-     api-key для теста - wNxRewGJZM2xe0xZgePsPB3BwOUjpsenRWXiIlQfEAsnOqR7NtkxtEeYMc41
- 		(выставить в файле API_key.py)





**I.** Первая реализация забора паролей находится в файле FrameWork_v1_0.py, сам тест в файле test_for_1_0.
Для тестирования функционала все переменные в environment(api_folder) уже выставлены.

Здесь реализована выдача одного дешифро-пароля под конкретного пользователя(доступны все группы и пароли,
но чтобы получить на выходе желаемый результат нужно указывать две переменные - логин и роль.

**Запуск:**
    Если установка прошла успешна и все зависимости соблюдены,
    то из корневой папки проекта запустить файл test_for_1_0 и получить на выходе файл password.json

**II.** Вторая реализация забора паролей находится в файле FrameWork_v1_1.py, сам тест в файле test_for_1_1.
Для тестирования функционала все переменные в environment(api_folder) уже выставлены.

_Здесь реализована выдача всех расшифрованных паролей вида_ - 
>                                     {
>                                       "user": {
>                                         "login": "password",
>                                         "login": "password",
>                                         "login": "password"
>                                       },
>                                       "admin": {
>                                         "login": "password",
>                                         "login": "password"
>                                       },
>                                       "security": {
>                                         "login": "password",
>                                         "login": "password",
>                                         "login": "password"
>                                       }
>                                     }


**Запуск:**
    Если установка прошла успешна и все зависимости соблюдены,
    то из корневой папки проекта запустить файл test_for_1_1.py и получить на выходе файл passwords.json

                Файл **passwords.json** оставлен для демонстрации реализации, перед запуском теста **удалить**!
