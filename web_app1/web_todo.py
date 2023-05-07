import streamlit as st
import functions_for_cli

todos = functions_for_cli.get_todos()


def add_todo():
    todo_added = st.session_state["new_todo"] + "\n"
    todos.append(todo_added)
    functions_for_cli.write_todos(todos)


st.title("My Todo App", )
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions_for_cli.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
