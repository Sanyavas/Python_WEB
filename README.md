[![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dark)](https://github.com/sanyavas/github-readme-quotes)

### Technology which used:
![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

# Python Web 10

## Використання `main.py` як єдиної точки входу

`main.py` це файл, який є точкою входу для вашого проекту. Це означає, що коли ви запускаєте ваш проект, інтерпретатор Python починає виконувати код цього файлу. Це може бути корисним, тому що вам не потрібно запускати кожен файл окремо, а можете використовувати одну точку входу для запуску всієї програми.

Щоб об'єднати файли в проекті, можна імпортувати функції або класи з інших файлів у `main.py`. Це може виглядати так:

```python
from my_module import my_function

def main():
    my_function()

if __name__ == "__main__":
    main()
```

У цьому прикладі ми імпортуємо функцію `my_function` з файлу `my_module.py` і викликаємо її в функції `main()`. Потім ми перевіряємо, чи запущено цей файл як основний скрипт, і якщо так, ми запускаємо функцію `main()`. Це дозволяє використовувати цей файл як модуль інших скриптів, не запускаючи функцію `main()`, якщо він імпортований як модуль.

Ви також можете використовувати `main.py` для об'єднання та організації вашого коду, наприклад, імпортуючи різні класи та функції з різних файлів та використовуючи їх для створення програмного інтерфейсу або для запуску різних функцій у певному порядку. Це може допомогти вам зберегти ваш код у порядку і легко знайти потрібний код у майбутньому.

Допустимо, у вас є простий проект, який складається з трьох файлів: `main.py`, `data.py` та `processing.py`.

`data.py` містить функцію для завантаження та обробки даних, `processing.py` містить функцію для аналізу даних, а `main.py` служить як точка входу для проекту.

У файлі `main.py` ви можете імпортувати функції з `data.py` та `processing.py` та використовувати їх для обробки даних та аналізу:

```python
from data import load_data
from processing import analyze_data

def main():
    data = load_data()
    analyze_data(data)

if __name__ == "__main__":
    main()
```

У цьому прикладі функція `load_data` з `data.py` використовується для завантаження та обробки даних, а функція `analyze_data` з `processing.py` використовується для аналізу даних. Потім функція `main` викликається для запуску проекту.

Це простий приклад, але він демонструє, як ви можете використовувати `main.py` для об'єднання різних функцій та модулів в одному місці та організації вашого коду. Ви можете додавати додаткові функції та модулі до вашого проекту і використовувати main.py для об'єднання їх всього в одному місці. Це допоможе вам зберегти ваш код у порядку і легко знайти потрібний код у майбутньому.

Коротше, коли створюєш код, думай як через `main.py` ти шукатимеш свої файли в 
проекті, переходячи по ним як по сторінкам веб-сайту.

## Деякий підсумок до вебінару по Docker

### Робота з контейнерами

По-перше, вам потрібно встановити **Docker** на вашій машині. Ви можете завантажити його з офіційного веб-сайту, якщо ви цього ще не зробили.

Щоб запустити контейнер за базою **MongoDB**, ви можете використати команду `docker run`.

Наприклад:

```bash
docker run -d -p 27017:27017 --name my-mongo mongo
```

Ця команда запустить новий контейнер у відокремленому режимі демона `-d` і зіставить порт `27017` локальної машини (хоста) з портом `27017` контейнера `-p 27017:27017`. Прапорець `--name` призначає назву контейнеру, а `mongo` — це ім’я зображення з Docker Hub.

<https://hub.docker.com/_/mongo>

Щоб отримати доступ до контейнеру **MongoDB**, ви можете скористатися командою `docker exec`.

Наприклад:

```bash
docker exec -it my-mongo /bin/sh
```

Ця команда відкриє термінал `sh` всередині контейнера під назвою `my-mongo`.

Щоб зберегти дані, можна використовувати томи.

```bash
docker run -d -p 27017:27017 -v d/data/db:/data/db --name my-mongo mongo
```

Ця команда відобразить каталог `d/data/db` локальної машини в каталог `/data/db` контейнера, де **MongoDB** зберігає свої дані.

Після запуску контейнера ви можете використовувати оболонку **MongoDB Compass** для підключення до екземпляра **MongoDB** і створення та керування базами даних.

Щоб запустити контейнер, можна використовувати команду `docker start` з ім'ям або унікальним ідентифікатором контейнера.

Наприклад:

```bash
docker start my-mongo
```

Щоб зупинити контейнер, можна використовувати команду `docker stop` з ім'ям або унікальним ідентифікатором контейнера. Наприклад:

```bash
docker stop my-mongo
```

Ви можете використовувати команду `docker ps`, щоб переглянути запущені контейнери та їх статус. І команду `docker ps -a` щоб переглянути всі контейнери, запущені та зупинені.

### Наш застосунок як контейнер

Застосунок.

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return """
        <h1>Hello World!</h1>
        <p style="color:crimson">Group web <b>10</b></p>
        """


if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Неважливе пояснення, що робить цей код:

>Цей код створює простий `Flask` додаток з єдиним маршрутом, який повертає рядок коли до нього звертаються на адресу 'http://localhost:5000/'.
>У рядку `app = Flask(__name__)` створюється екземпляр `Flask` класу і надається змінної `app`.
> Декоратор `@app.route('/')` створює маршрут кореневої адреси `'/'`, який буде пов'язаний з функцією `hello()`. Функція `hello()` повертає рядок.
> Якщо ім'я скрипта дорівнює `main`, програма запускається з налаштуванням `host='0.0.0.0'`, що означає, що програма буде доступна для доступу з будь-якої адреси.

Dockerfile

```dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]
```

 код використовується для створення образу Docker.

- `FROM python:3.10` вказує, що образ буде заснований на офіційному образі Python 3.10.
- `WORKDIR /app` встановлює поточний робочий каталог `/app`.
- `COPY . .`  копіює всі файли з поточного каталогу на локальній машині до поточного робочого каталогу всередині контейнера.
- `RUN pip install -r requirements.txt` встановлює всі залежності, вказані у файлі `requirements.txt` у контейнер.
- `EXPOSE 5000` вказує, що контейнер прослуховуватиме порт `5000`.
- `ENTRYPOINT ["python", "main.py"]` вказує, що команда python `main.py` буде запущена під час запуску контейнера. Це запускає вашу програму на сервері.

Щоб тепер створити образ **Docker** за допомогою файлу `Dockerfile`, ви можете використовувати команду `docker build`. Команда має такий формат:

```bash
docker build [path_to_dockerfile] -t [image_name]:[tag]
```

`-t` вказує ім'я та тег для нового образу.
`[path_to_dockerfile]` вказує місце, де знаходиться файл `Dockerfile`.

Приклад:

```bash
docker build . -t myapp:latest
```

Ця команда створить образ з ім'ям `myapp` та тегом `latest` на основі файлу `Dockerfile` у поточній директорії.

Після створення образу ви можете запустити контейнер за допомогою команди `docker run`

```bash
docker run -p 80:5000 myapp
```

Ця команда запустить контейнер з ім'ям `myapp`, прив'язавши порт `5000` внутрішнього контейнера до порту `80` на машині.

Тепер посилання на додаток <http://localhost/>
