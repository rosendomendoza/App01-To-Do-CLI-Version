import functions

def show_todos():
    todos = functions.get_todos()
    print()
    print("Things To Do:")
    for index, item in enumerate(todos):
        row = f"{index + 1}-{item}"
        print(row.strip('\n'))
    print()


print()
print("ToDo App - CLI version")
print("**********************")

while True:
    show_todos()
    user_action = input("Enter an option <add, edit, complete or exit>: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todos = functions.get_todos()
        todo = user_action[4:].strip()

        if len(todo) > 0:
            todo = todo + '\n'
            todos.append(todo)
            functions.write_todos(todos)
        else:
            print("Nothing to add. Try again.")

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            index = int(user_action[5:])
            index -= 1
            print("ToDo to edit: ",todos[index].strip("\n"))
            todo = input("Enter the change: ") + '\n'
            todos[index] = todo
            functions.write_todos(todos)

        except:
            print("The task don't exist. Try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            index = int(user_action[9:])
            index -= 1
            todo_rem = todos[index].strip("\n")
            confirm_task = input(f'To confirm type "{todo_rem}":')

            if todo_rem == confirm_task:
                todos.pop(index)
                msj = f"The task '{todo_rem}' was remove successfully \n"
                print(msj)
                functions.write_todos(todos)
            else:
                print("Conformation error. Try again.")

        except:
            print("The task number don't exist. Try again.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid...")

print("Bye..!")
