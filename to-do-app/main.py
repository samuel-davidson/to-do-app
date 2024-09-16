def main():
    first_message()
    name = input().capitalize()
    print_hi(name)
    enter_to_do()
    to_do_item = input()
    List = ToDo()
    List.add_task(to_do_item)
    print(List)


def print_hi(name):
    return print(f'Hi {name}!')


def first_message():
    return print("Please enter your name.")


def enter_to_do():
    return print("Please enter a task:")

class ToDo:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)
        return (print(f'You have added {task} to your To-Do list'))

    def remove_task(self, task):
        self._tasks.remove(task)

if __name__ == "__main__":
    main()