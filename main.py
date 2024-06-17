import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

def send_email():
    # Настройки отправителя и получателя
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    password = "your_email_password"

    # Настройки письма
    subject = "Ежедневный отчет"
    body = "Пожалуйста, найдите прикрепленный отчет за сегодня."

    # Создание сообщения
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Добавление текста письма
    message.attach(MIMEText(body, "plain"))

    # Присоединение файла
    filename = "report.pdf"  # Путь к вашему отчету
    attachment = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)

    # Настройка соединения и отправка письма
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.example.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    attachment.close()
    print("Email sent successfully!")

# Планирование ежедневной отправки отчета в 9 утра
schedule.every().day.at("09:00").do(send_email)

# Бесконечный цикл для выполнения запланированных задач
while True:
    schedule.run_pending()
    time.sleep(1)
