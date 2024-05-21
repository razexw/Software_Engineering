def is_polindrome(data):
    return data == data[::-1]

def main():
    data = input()
    if is_polindrome(data):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()