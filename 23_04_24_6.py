def strip_punctuation_ru(data):
    punctuation = '!"#$%\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuation:
        data = data.replace(char, '')
    return data

def test_strip_punctuation_ru():
    test_data = input("Введите текст на русском: ")
    result = strip_punctuation_ru(test_data)
    if result:
        print(result)
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    test_strip_punctuation_ru()