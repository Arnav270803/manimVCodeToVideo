import streamlit as st
import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("To-Do List")

new_task = st.text_input("Enter new task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        save_tasks(st.session_state.tasks)
        st.success("Task added!")
        st.rerun()

    else:
        st.warning("Please enter a task.")

if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"{i+1}. {task}")
else:
    st.write("No tasks found.")
