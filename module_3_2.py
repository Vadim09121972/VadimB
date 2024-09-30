def send_email (message, recipient, sender = "university.help@gmail.com"):
    if ('@' or '.com' or '.ru' or '.net') not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе")
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else: #elif sender != "university.help@gmail.com":     
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    
send_email('messagie', 'gor.job')
send_email('messagie', "university.help@gmail.com")
send_email('messagie', 'bob@top.com') 
send_email('messagie', 'universitay.help@gmail.com', 'ghg.com')