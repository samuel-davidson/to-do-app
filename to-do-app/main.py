def main():
    to_do_list = ToDo()
    check_in()
    primary_user_interaction(to_do_list)


def check_in():
    # note
    print("Please enter your name.")
    name = input().capitalize()
    return print(f'Hi {name}!')


def primary_user_interaction(to_do_list):
    while True:
        user_choice = input(
            "Enter 'add', 'show', 'edit', 'complete', or 'exit': "
            ).capitalize()
        user_choice = user_choice.strip()
        match user_choice:
            case 'Add':
                to_do_item = input(
                    "Enter a new task: "
                    ).capitalize()
                to_do_list.add_task(to_do_item)
            case 'Edit':
                to_do_item_idx = int(input(
                    "Enter the task # to edit: "
                    ))
                if to_do_list.contains_task(to_do_item_idx) is False:
                    print('Task not in list')
                else:
                    item_update = input(
                        "Enter the updated task: ").capitalize()
                    to_do_list.edit_task(to_do_item_idx, item_update)
            case 'Show' | 'Display':
                to_do_list.show_list()
            case 'Exit':
                break
            case 'Complete':
                to_do_item_idx = int(input(
                    "Enter the task # to complete: "
                    ))
                to_do_list.remove_task(to_do_item_idx)
            case unknown:
                print("You entered an unknown command")


class ToDo:
    def __init__(self):
        self._tasks = ["To-Do List:"]

    def add_task(self, task):
        self._tasks.append(task)
        return print(f'You have added "{task}" to your To-Do list')

    def contains_task(self, task_idx):
        if task_idx >= len(self._tasks):
            return False
        if task_idx == 0:
            return False
        else:
            return True

    def edit_task(self, task_idx, update):
        task = self._tasks[task_idx]
        self._tasks[task_idx] = update
        return print(
            f'You have updated "{task}" to "{update}" on your To-Do list'
            )

    def remove_task(self, task_idx):
        task = self._tasks[task_idx]
        self._tasks.pop(task_idx)
        print(f'"{task}" removed from list')

    def show_list(self):
        count = 0
        for item in self._tasks:
            if item is not None:
                if item != "To-Do List:":
                    print(f'{count} - {item}')
                    count += 1
                else:
                    print(item)
                    count += 1


if __name__ == "__main__":
    main()
