import sys

def main():
    print("プログラムに渡された引数:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"引数 {i}: {arg}")

if __name__ == "__main__":
    main()
