def strip_punctuation_ru(data):
   punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
   for char in punctuation:
       data = data.replace(char, '')
   return ' '.join(data.split())

def is_passed(test_result):
   if test_result:
       print("YES")
   else:
       print("NO")

def test_strip_punctuation_ru():
   test_data = [
       "Привет, как дела?",
       "Я люблю путешествовать!",
       "Какой сегодня прекрасный день?"
   ]
   expected_results = [
       "Привет как дела",
       "Я люблю путешествовать",
       "Какой сегодня прекрасный день"
   ]

   for i in range(len(test_data)):
       result = strip_punctuation_ru(test_data[i])
       is_passed(result == expected_results[i])

def main():
   test_strip_punctuation_ru()

if __name__ == '__main__':
   main()