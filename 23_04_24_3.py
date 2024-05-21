def is_correct_mobile_phone_number_ru(number):
    number = ''.join(filter(str.isdigit, number))
    if str(number[0]) == "8" or str(number[0] == "7"):
        if len(number) == 11:
            return True
        else:
            return False

def test():
    tests = ["+7(900)1234567", "8(900)123-45-67", "+79991234567", "+7 (999) 123-45-67", "8(999)1234567", "89001234567", "+7(926)1234567", "1234567"]
    for number in tests:
        if is_correct_mobile_phone_number_ru(number):
            print(f"{number}: YES")
        else:
            print(f"{number}: NO")

def main():
    test()

if __name__ == '__main__':
    main()