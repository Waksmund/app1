FILEPATH = 'todos.txt' #constants

def get_todos(filepath=FILEPATH):
    #docstring
    """  
    Docstring for get_todos
    
    :param filepath: path to the file containing stored todos
    
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Docstring for write_todos
    
    :param todos_arg: list of todos to store
    :param filepath: path to the file containing stored todos

    Write todos to file
    """
    with open(filepath, 'w') as file:
            file.writelines(todos_arg)

print(__name__)
#code inside the if statment will not be executed at the import of functions module only when we run directly the functions file
if __name__ == "__main__":
    print("Hello")