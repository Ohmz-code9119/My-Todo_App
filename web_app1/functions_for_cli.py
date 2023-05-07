FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the list of
    to-do items
    """
    with open(filepath, 'r') as file_read:
        todos_fileread = file_read.readlines()
    return todos_fileread


def write_todos(todos_arg, filepath=FILEPATH):
    """write tod-do items in a text file"""
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from function for main")
