from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib, os
import random

load_dotenv('.env')

def generate_num():
    return random.randint(100000, 999999)

def send_email(email):
    code = generate_num()
    message = f"Ваш код: {code}"
    send_message("Подтверждение", message, email)
    return code

def check_code(code, num_code):
    if code == num_code:
        return "Вы успешно зарегистрировались"
    else:
        return "Неправильный код подтверждения"
    
def end():
    email = input("Введите вашу почту: ")
    code = send_email(email)
    attempts = 3
    while attempts > 0:
        num_code = input("Введите код подтверждения: ")
        result = check_code(code, int(num_code))
        if result == "Вы успешно зарегистрировались":
            print(result)
            break
        else:
            attempts -= 1
            print(f"Неправильно. Осталось {attempts} попыток")
    if attempts == 0:
        print("Слишком много попыток")

def send_message(title:str, message:str, to_email:str) -> bool:
    sender = os.environ.get('smtp_email')
    password = os.environ.get('smtp_password')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = EmailMessage()
        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = to_email
        msg.set_content(message)
        server.send_message(msg)
        return True
    except Exception as error:
        return {False:error}
print(send_message('Emir Hello', 'Hello Backend Geeks', '20adinka09@gmail.com'))

end()