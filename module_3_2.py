
def is_address_valid(email: str) -> bool:
    if '@' not in email:
        return False

    remail = email[::-1].lower()
    for domain in [".com", ".ru", ".net"]:
        if remail.find(domain[::-1]) == 0:
            return True

    return False


def send_email(message, recipient, *, sender = 'university.help@gmail.com') -> None:
    if not is_address_valid(recipient) or not is_address_valid(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return

    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


def test():
    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
#Вывод на консоль:
#Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
#НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
#Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
#Нельзя отправить письмо самому себе!


def main():
    send_email('', '')
    send_email('jkhfqwalsnh;qwerjfhbn', '@.com')
    send_email('akljkasjaskjas', '@.cococo')
    send_email('', '@.ru', sender='urban.info@gmail.com')
    send_email('1', '@ыыыыыыыы.net', sender='http://yandex.ru/free_cat_pictures_no_sms.html urban@info.com')
    send_email("pycckuu' 93blk", 'urban.fan@mail.соm')
    send_email("самому себе",     'university.help@gmail.com', sender='university.help@gmail.com')
    send_email("ещё самому себе", 'university.help@gmail.com', sender='university.help@gmаil.com')
    send_email("а так?",          'university.help@gmаil.com', sender='university.help@gmail.com')


test()
#main()

"""
2023/10/08 00:00|Домашняя работа по уроку "Способы вызова функции"

Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.

Задача "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
Проверка на корректность e-mail отправителя и получателя.
Проверка на отправку самому себе.
Проверка на отправителя по умолчанию.
Пункты задачи:
Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

Пример результата выполнения программы:
Пример выполняемого кода (тесты):
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
Вывод на консоль:
Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
Нельзя отправить письмо самому себе!

Примечания:
Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
Именованные аргументы всегда идут после позиционных.

Файл module_3_2.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""