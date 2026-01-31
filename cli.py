#todos = []
from functions import get_todos, write_todos #a few functions in teh functions file/module
#or (many functions)
#import functions /from directory import
#and call them by function     module:
#functions.get_todos()

import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's: ", now)

#docstring/multiline string -> write multiline text (no need for breaklines characters \n)
a="""
Principles of productivity:
Manage your inflow.
Systemizing everything that repeats.
"""


while True:
    user_action = input("Type (a)dd, (s)how, (e)dit, (c)omplete or e(x)it: ").strip()
    i = 0
    # match user_action:
    #     case 'a':
    
    #if 'add' in user_action[:3]:
    if user_action.startswith("add"):
        # todo = input("Enter a todo: ") + "\n"
        
        todo = user_action[4:] + "\n" #list slicing [a:b]

        # file = open('.venv/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        todos.append(todo)

        # file = open('.venv/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)
            
    elif user_action.startswith('show'):
        todos = get_todos()

        #  new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
            
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # print(f"{index}. {item[:-1]}")
            print(f"{index}. {item.strip('\n')}")
    elif user_action.startswith('edit'):
        # number = int(input("number of the chore to edit: "))
        # new_todo = input("Enter a new todo: ") + "\n"
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter a new todo: ") + "\n"

            todos[number] = new_todo

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        # todo_num = int(input("Please enter the number of todos to delete: "))
        try:
            todo_num = int(user_action[9:])
            
            todos = get_todos()

            del_item = todos.pop(todo_num)
            print(del_item.strip('\n'), "has been deleted")

            write_todos(todos)
            
        except IndexError:
            print("There's no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    # case _:
    else:
            print("You entered a wrong command!")
print("Bye!")
    
