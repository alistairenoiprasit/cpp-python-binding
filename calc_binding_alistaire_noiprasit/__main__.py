from .calculator import Calculator


def main():
    print("Hi I am from main")
    print(Calculator().add(1, 2))
    return 0


if __name__ == "__main__":
    main()