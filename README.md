##Настройка скрипта

**1. Установка необходимых библиотек:**
Убедитесь, что у вас установлены библиотеки schedule и smtplib. Для установки schedule выполните:
    `pip install schedule`

**2. Настройка учетных данных:**
Введите свои учетные данные электронной почты и пароль:
    `sender_email = "your_email@example.com"`
    `password = "your_email_password"`

**3. Настройка SMTP-сервера:**
Замените "smtp.example.com" на SMTP-сервер вашего почтового провайдера (например, для Gmail это будет "smtp.gmail.com"):
    `with smtplib.SMTP_SSL("smtp.example.com", 465, context=context) as server:`

**4. Путь к отчету:**
Убедитесь, что файл отчета находится в указанном месте, или измените путь к файлу:
    `filename = "report.pdf"`

**5. Настройка времени отправки:**
Измените время в строке schedule.every().day.at("09:00").do(send_email) на нужное вам. Формат времени - "HH
" в 24-часовом формате.
