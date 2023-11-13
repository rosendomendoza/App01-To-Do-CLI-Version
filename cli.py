import functions

while True:
    user_action = input("add, show, edit, complete or exit: ")
    user_action  = user_action.strip()

    if user_action.startswith("add"):
        todos = functions.get_todos()
        todo = user_action[4:].strip()
        if len(todo) > 0:
            todo = todo + '\n'
            todos.append(todo)
            functions.write_todos(todos)
        else:
            print("Nada que añadir")

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item}"
            print(row.strip('\n'))

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            index = int(user_action[5:])
            index -= 1
            print("Actividad a Modificar: ",todos[index].strip("\n"))
            todo = input("Ingrese los cambios: ") + '\n'
            todos[index] = todo
            functions.write_todos(todos)

        except:
            print("Comando equivocado. Intenete de nuevo.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            index = int(user_action[9:])
            index -= 1
            todo_rem = todos[index].strip("\n")
            todos.pop(index)
            msj = f"La actividad '{todo_rem}' fue removida de la lista de cosas por hacer \n"
            print(msj)
            functions.write_todos(todos)

        except IndexError:
            print("Nro de Actividad no Valido. Intente de nuevo.")
            continue

        except ValueError:
            print("Indique el Id de la actividad completada.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid...")
print("Adios..!")
