import sys

def main():
    if len(sys.argv) == 3:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            result = num1 + num2
            print(result)
        except (IndexError, ValueError):
            print(0)
    else:
        print(0)

if __name__ == "__main__":
    main()