def is_polindrome(data):
    return data == data[::-1]

def test():
    tests = ["", "a", "aba", "шалаш", "радар", "madam", "level", "ананас", "banana"]
    for data in tests:
        if is_polindrome(data):
            print(f"YES")
        else:
            print(f"NO")
def main():
    test()

if __name__ == '__main__':
    main()