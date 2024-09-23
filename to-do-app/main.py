def main():
    to_do_list = ToDo()
    first_message()
    name = input().capitalize()
    print_hi(name)
    enter_to_do(to_do_list)

def print_hi(name):
    return print(f'Hi {name}!')


def first_message():
    return print("Please enter your name.")


def enter_to_do(to_do_list):
    print("Please enter your tasks and enter 'Done' when finished.")
    while True:
        print("Task:")
        to_do_item = input().capitalize()
        if to_do_item == "Done":
            break
        to_do_list.add_task(to_do_item)
        to_do_list.show_list()
    to_do_list.show_list()
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