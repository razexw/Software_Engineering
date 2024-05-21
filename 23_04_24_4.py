def is_correct_mobile_phone_number_ru(number):
    number = ''.join(filter(str.isdigit, number))
    if number.startswith("8") or number.startswith("7"):
        if len(number) == 11:
            print(f"YES")
            return True
    print(f"NO")
    return False

def main():
    number = input()
    is_correct_mobile_phone_number_ru(number)

if __name__ == '__main__':
    main()