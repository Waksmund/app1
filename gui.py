import functions
import time

import FreeSimpleGUI as sg
sg.theme("Black")

time_label = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo") 
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                    layout=[[time_label],
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_button, complete_button], 
                            [exit_button]], 
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200) #returned by the window ('Add, {'todo', 'user input'})
    # print("Event: ", event)
    # print("Values: ", values)
    
    if event == 'todos':
        window['todo'].update(values['todos'][0].replace("\n", ""))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos() #pobranie listy
                todo_to_edit =  values['todos'] #zadanie do edycji
                # print(todos)
                # print(str(todo_to_edit[0]))
                ind = todos.index(todo_to_edit[0]) #index zadania do edycji
                new_todo = values['todo'] + "\n"
                # print(todos)
                # print(ind)
                # print(todo_to_edit)
                todos[ind] = new_todo #edycja zadania
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16))
        case "Complete":
            try:
                todos = functions.get_todos() #pobranie listy
                todo_to_complete =  values['todos'] #zadanie do edycji
                # print(todos)
                # print(str(todo_to_edit[0]))
                ind = todos.index(todo_to_edit[0])
                todos.remove(todos[0])
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update("")
            except NameError:
                sg.popup("Please select an item first", font=("Helvetica", 16))
        case (sg.WIN_CLOSED | "Exit"):
            break
    window["clock"].update(value=time.strftime("%H:%M:%S"))
window.close()