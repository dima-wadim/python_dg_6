# pythonProject_Django
Курсовой проект по теме Django.

Сервис управления рассылками, администрирования и получения статистики
Установка: Перед началом установки убедитесь, что у вас установлен Python 3.11 и Pip (пакетный менеджер для Python).

Установите зависимости с помощью pip: pip install

Основная логика работы приложения:
1)После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
2)Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
3)По ходу отправки сообщений должна собираться статистика по каждому сообщению для последующего формирования отчетов.
4)Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы.  Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

Для запуска рассылок со временем старта в будущем необходимо воспользоваться django_apcheduller. Подробнее про то как его запустить можно посмотреть здесь https://pypi.org/project/django-apscheduler/.

Для отработки кеширования необходимо установать redis и запустить его. Подробнее о том, как можно запустить redis из Windows можно ознакомиться здесь https://redis.io/docs/getting-started/installation/install-redis-on-windows/.
Сервис управления рассылками, администрирования и получения статистики
Установка: Перед началом установки убедитесь, что у вас установлен Python 3.11 и Pip (пакетный менеджер для Python).
### Инструкция по развертыванию:
1.Склонируйте проект: 
2. Создайте вертуальное окружение: python3 -m venv venv 
3. Активируйте вертуальное окружение: venv/Scripts/activate.bat
4. Установите зависимости с помощью pip:  pip3 install -r .\requirements.txt
5. Создайте файл .env из шаблона .env.example
6. Примените миграции: python manage.py migrate
7. Запустите проект: python manage.py runserver
 
