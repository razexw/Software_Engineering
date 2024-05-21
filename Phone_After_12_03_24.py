class PhoneFormatException(Exception):
    pass

def check_phone(phone):
    try:
        phone = "".join(phone.split())
        if phone.find("+7") != 0 and phone.find("8") !=0 and phone.find("+359") != 0 and phone.find("+1") != 0 and phone.find("+55") != 0:
            raise PhoneFormatException("Неверный формат")
        if not all(phone.split("-")):
            raise PhoneFormatException("Неверный формат")
        else:
            phone = phone.replace("-", "")
            start_bt = phone.find("(")
            end_bt = phone.find(")")
        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1: end_bt].isdigit() or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise PhoneFormatException("Неверный формат")
        elif end_bt > -1:
            raise PhoneFormatException("Неверный формат")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        if phone.find("8") == 0:
            phone = "+7" + phone[1:]
        if not phone[1:].isdigit():
            raise PhoneFormatException("Неверный формат")
        if phone.find("+7") == 0:
            if not len(phone[1:]) == 11:
                raise PhoneFormatException("Неверное количество цифр")
            if ((int(phone[2:5]) >= 910 and int(phone[2:5]) <= 919) or (int(phone[2:5]) >= 980 and int(phone[2:5]) <= 989)):
                raise PhoneFormatException("МТС")
            elif (int(phone[2:5]) >= 920 and int(phone[2:5]) <= 939):
                raise PhoneFormatException("Мегафон")
            elif ((int(phone[2:5]) >= 902 and int(phone[2:5]) <= 906) or (int(phone[2:5]) >= 960 and int(phone[2:5]) <= 969)):
                raise PhoneFormatException("Билайн")
            else:
                raise PhoneFormatException("Не определяется сотовый оператор")
        elif phone.find("+359") == 0:
            if not len(phone[1:]) == 13:
                raise PhoneFormatException("Неверное количество цифр")
            return phone
        elif phone.find("+55") == 0:
            if not len(phone[1:]) == 12:
                raise PhoneFormatException("Неверное количество цифр")
            return phone
        elif phone.find("+1") == 0:
            if not len(phone[1:]) == 11:
                raise PhoneFormatException("Неверное количество цифр")
            return phone
        else:
            raise PhoneFormatException("Не определяется код страны")
    except PhoneFormatException as e:
        return e

try:
    result = check_phone(input())
    print(result)
except PhoneFormatException as e:
    print(e)