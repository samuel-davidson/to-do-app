def main():
    to_do_list = ToDo()
    check_in()
    primary_user_interaction(to_do_list)


def check_in():
    print("Please enter your name.")
    name = input().capitalize()
    return print(f'Hi {name}!')


def primary_user_interaction(to_do_list):
    while True:
        user_choice = input("Enter 'add', 'show', or 'exit': ")
        match user_choice:
            case 'add':
                to_do_item = input("Enter a new task: ").capitalize()
                to_do_list.add_task(to_do_item)
            case 'show':
                to_do_list.show_list()
            case 'exit':
                break


class ToDo:
    def __init__(self):
        self._tasks = ["To-Do List:"]

    def add_task(self, task):
        self._tasks.append(task)
        return print(f'You have added "' + task + '" to your To-Do list')

    def remove_task(self, task):
        self._tasks.remove(task)

    def show_list(self):
        for item in self._tasks:
            if item is not None:
                if item != "To-Do List:":
                    print(f'-' + item)
                else:
                    print(item)


if __name__ == "__main__":
    main()