# Bank security console

This is an internal repository for employees of Radiance Bank. If you got into
this repository by accident, you will not be able to run it, since you do not
have access to the database, but you can freely use the layout code or see
how queries to the database are implemented.

The security desk is a website that can be connected to a remote database with
business cards and access cards of our bank employees.

### How to install

Python3 should be already installed.

It is recommended to use a `.venv` virtual environment to isolate the project.:
```shell
> python -m venv .venv
```

Then use `pip` (or `pip3`, there is a conflict with Python 2) to install dependencies:
```shell
> pip install -r requirements.txt
```

In the file `.env.example` you can see the environment variables, they are used in the module `settings.py `
to configure and access the database. If you have access and the necessary data, you can rename
the `.env.example` file to `.env` and fill in the environment variables. `SECRET_KEY` is the secret key of the website.
`DB_URL` is a link with sensitive database data, which includes: user, password, host, port, name. 
`DB_URL` functions using the [dj-database-url](https://github.com/jazzband/dj-database-url/tree/master) 
library. The template for this environment variable looks like this: 
`postgres://myuser:mypassword@localhost:5432/mydatabase`. 
More information about the `dj-database-url` library can be found at the link above. 
If for some reason you do not want to use
`dj-database-url`, use standard environment variables to configure the database. The templates
are presented in the `.env.example` file. In this case, in the module `settings.py` the `DATABASES`
object should look like this:
```shell
DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD
    }
}
```

### Running the script

```shell
> python passcards.py
```

Output example:
```shell
employee_name: Jennifer Martin
passcode: ceb148a6-fb27-4106-890c-89dc8cedfe83
created_at: 2018-01-11 12:28:39+00:00
is_active: True

Всего пропусков 100
Активных пропусков 89
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка 'Сияние'. Если вы попали в
этот репозиторий случайно, то вы не сможете его запустить, так как у вас нет
доступа к БД, но можете свободно использовать код вёрстки или посмотреть
как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной базе данных с 
визитами и карточками пропуска сотрудников нашего банка.

### Как установить

Python3 должен быть уже установлен. 

Для изоляции проекта рекомендуется использовать `.venv` виртуальное окружение. 
```shell
> python -m venv .venv
```

Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```shell
> pip install -r requirements.txt
```

В файле `.env.example` можно ознакомиться с переменными окружения, они используются в модуле `settings.py`
для настройки и получения доступа к базе данных. Если у вас есть доступ и необходимые данные, можете переименовать
файл `.env.example` в `.env` и заполнить переменные окружения. `SECRET_KEY` - секретный ключ сайта.
`DB_URL` - ссылка с чувствительными данными базы данных, к данным относится: user, password, host, port, name. 
Функционирует при помощи библиотеки [dj-database-url](https://github.com/jazzband/dj-database-url/tree/master). 
Шаблон для данной переменной окружения выглядит следующим образом: 
`postgres://myuser:mypassword@localhost:5432/mydatabase`. Подробнее о библиотеке `dj-database-url` можно узнать по ссылке выше. 
Если вы не по каким либо причинам не хотите использовать
`dj-datavase-url`, используйте стандартные переменные окружения, для настройки базы данных, шаблоны
представлены в файле `.env.example`.
В таком случае, в модуле `settings.py` объект `DATABASES` должен выглядеть 
следующим образом: 
```shell
DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD
    }
}
```

### Запуск скрипта

```shell
> python passcards.py
```

Пример вывода:
```shell
employee_name: Jennifer Martin
passcode: ceb148a6-fb27-4106-890c-89dc8cedfe83
created_at: 2018-01-11 12:28:39+00:00
is_active: True

Всего пропусков 100
Активных пропусков 89
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).