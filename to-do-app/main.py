def main():
    first_message()
    name = input().capitalize()
    print_hi(name)
    enter_to_do()
    to_do_item = input()

def print_hi(name):
    return print(f'Hi {name}!')


def first_message():
    return print("Please enter your name.")


def enter_to_do():
    return print("Please enter a task:")


if __name__ == "__main__":
    main()