import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos('todos.txt')

        todos.append(todo + "\n")

        functions.write_todos("todos.txt", todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            output = f"{index + 1}. {item.capitalize()}"
            print(output)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos('todos.txt')

            new_todo = input("Enter new ToDo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"ToDo {todo_to_remove.capitalize()} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue

    elif 'exit' in user_action:
        break

    else:
        print("Command is not valid")

print('Bye!')