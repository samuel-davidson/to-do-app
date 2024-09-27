def main():
    to_do_list = ToDo()
    check_in()
    primary_user_interaction(to_do_list)


def check_in():
    #note
    print("Please enter your name.")
    name = input().capitalize()
    return print(f'Hi {name}!')


def primary_user_interaction(to_do_list):
    while True:
        user_choice = input("Enter 'add', 'show', 'edit' or 'exit': ").capitalize()
        match user_choice:
            case 'Add':
                to_do_item = input("Enter a new task: ").capitalize()
                to_do_list.add_task(to_do_item)
            case 'Edit':
                to_do_item = input("Enter the task to edit: ").capitalize()
                if to_do_list.contains_task(to_do_item) is False:
                    print('Task not in list')
                else:
                    item_update = input("Enter the updated task: ").capitalize()
                    to_do_list.edit_task(to_do_item, item_update)
            case 'Show' | 'Display':
                to_do_list.show_list()
            case 'Exit':
                break
            case unknown:
                print("You entered an unknown command")


class ToDo:
    def __init__(self):
        self._tasks = ["To-Do List:"]

    def add_task(self, task):
        self._tasks.append(task)
        return print(f'You have added "' + task + '" to your To-Do list')

    def contains_task(self, task):
        for el in self._tasks:
            if el == task:
                return True
        return False

    def edit_task(self, task, update):
        for idx, n in enumerate(self._tasks):
            if n == task:
                self._tasks[idx] = update
                return print(f'You have updated "' + update + '" on your To-Do list')

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