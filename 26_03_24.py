########################################################### 1

def pass_check(word):
    if len(word) <= 8:
        return False

    has_low = any(a.islower() for a in word)
    has_upp = any(a.isupper() for a in word)
    has_dig = any(a.isdigit() for a in word)
    keyboard = {"qwertyuiop", "йцукенгшщзхъ", "asdfghjkl", "фывапролджэ", "zxcvbnm", "ячсмитьбю"}
    three_in_a_row = any(word[i:i + 3].lower() in keyboard for i in range(len(word) - 2))

    if not has_dig:
        return False

    if three_in_a_row:
        return False

    if not (has_low and has_upp):
        return False

    return True


password = input("Введите пароль: ")
if pass_check(password):
    print("ok")
else:
    print("error")


########################################## 2

class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_pass(word):
    if len(word) < 9:
        raise LengthError("Длина пароля должна быть более 8 символов.")

    has_low = any(a.islower() for a in word)
    has_upp = any(a.isupper() for a in word)
    has_dig = any(a.isdigit() for a in word)
    keyboard = ["qwertyuiop", "йцукенгшщзхъ", "asdfghjkl", "фывапролджэ", "zxcvbnm", "ячсмитьбю"]

    if not has_dig:
        raise DigitError("Пароль должен содержать хотя бы одну цифру.")

    for i in range(len(word) - 2):
        if any(word[i:i + 3].lower() in row for row in keyboard):
            raise SequenceError("Символы пароля не должны идти подряд")

    if not (has_low and has_upp):
        raise LetterError("Пароль должен содержать символы разных регистров.")

    return "ok"


password = input("Введите пароль: ")
try:
    result = check_pass(password)
    print(result)
except PasswordError as e:
    print("error:", e)

################################### 3

class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_pass(word):
    assert len(word) >= 9, "Длина пароля должна быть более 8 символов."

    has_low = any(a.islower() for a in word)
    has_upp = any(a.isupper() for a in word)
    has_dig = any(a.isdigit() for a in word)
    keyboard = ["qwertyuiop", "йцукенгшщзхъ", "asdfghjkl", "фывапролджэ", "zxcvbnm", "ячсмитьбю"]

    assert has_dig, "Пароль должен содержать хотя бы одну цифру."

    for i in range(len(word) - 2):
        assert not any(word[i:i + 3].lower() in row for row in keyboard), "Символы пароля не должны идти подряд."

    assert has_low and has_upp, "Пароль должен содержать символы разных регистров."

    return "ok"


password = input("Введите пароль: ")
try:
    result = check_pass(password)
    print(result)
except AssertionError as e:
    print("error:", e)
except Exception as e:
    print("error:", e)


####################################### 4
class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_pass(word):
    assert len(word) >= 9, "Длина пароля должна быть более 8 символов."

    has_low = any(a.islower() for a in word)
    has_upp = any(a.isupper() for a in word)
    has_dig = any(a.isdigit() for a in word)
    keyboard = ["qwertyuiop", "йцукенгшщзхъ", "asdfghjkl", "фывапролджэ", "zxcvbnm", "ячсмитьбю", "poiuytrewq",
                "ъхзщшгнекуцй", "lkjhgfdsa", "эждлорпавыф", "mnbvcxz", "юбьтимсчя"]

    assert has_dig, "Пароль должен содержать хотя бы одну цифру."

    for i in range(len(word) - 2):
        assert not any(word[i:i + 3].lower() in row for row in keyboard), "Символы пароля не должны идти подряд"

    assert has_low and has_upp, "Пароль должен содержать символы разных регистров."

    return "ok"


while True:
    password = input("Введите пароль: ")
    try:
        if password.lower() == "ctrl+break":
            raise KeyboardInterrupt
        result = check_pass(password)
        print(result)
        break
    except AssertionError as e:
        print("error:", e)
    except Exception as e:
        print("error:", e)
    except KeyboardInterrupt:
        print("\nBye-Bye")
        break


########################################### 5

class DefaultList(list):
    def __init__(self, default):
        self.default = default
        super().__init__()

    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return self.default