import sys

def main():
    args = sys.argv[1:]
    do_sort = False

    if '--sort' in args:
        do_sort = True
        args.remove('--sort')

    parsed_args = [arg.split('=') for arg in args]

    if do_sort:
        parsed_args.sort(key=lambda x: x[0])

    for key, value in parsed_args:
        print(f"Key: {key} Value: {value}")

if __name__ == "__main__":
    main()