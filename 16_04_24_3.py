import sys

def main():
    if len(sys.argv) == 4:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            operator = sys.argv[3]

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            else:
                print("Invalid operator:", operator)
                return

            print(result)

        except (IndexError, ValueError) as e:
            print(e.__class__.__name__)
    else:
        print("0")

if __name__ == "__main__":
    main()