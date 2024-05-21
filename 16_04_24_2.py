import sys

def main():
    if len(sys.argv) <= 1:
        print("NO PARAMS")
    else:
        total = 0
        sign = 1
        for arg in sys.argv[1:]:
            try:
                num = int(arg)
                total += num * sign
                sign *= -1
            except ValueError as e:
                print(e.__class__.__name__)
                return
        print(total)

if __name__ == "__main__":
    main()