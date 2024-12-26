import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)  
    args = parser.parse_args()

    def count_lines(filename):  
        with open(filename, 'r') as f: 
            print(sum(1 for _ in f))
    def main():
        count_lines(args.file)
    if __name__ == "__main__":
        main()
except FileNotFoundError:  
    print(0)
except Exception as e: 
    print(f"An error occurred: {e}")