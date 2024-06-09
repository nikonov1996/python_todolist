import tkinter as tk
from tkinter import ttk, W, NO, VERTICAL, NW, N, SOLID, RIGHT, Y, X, E, S
from tkinter import END, BOTH
from tkinter.messagebox import showinfo
import db.todolist_db_provider as db
import gui.config as gui_conf


def drowModal(row):
    show_todo = tk.Tk()
    title = row[1]
    content = row[2]
    date = row[3]
    show_todo.geometry(gui_conf.size)
    show_todo.title(f"{title} {date}")

    content_todo_frame = ttk.Frame(show_todo,borderwidth=0, relief=SOLID, padding=[5, 5])

    titleText = tk.Text(content_todo_frame, wrap="word")
    titleText.configure(height=1)
    titleText.insert(tk.END, title)
    titleText.pack(fill=X)
    contentText = tk.Text(content_todo_frame, wrap="word")
    contentText.configure(height=15)
    contentText.insert(tk.END, content)
    contentText.pack(fill=X)

    content_todo_frame.pack(fill=BOTH,expand=True)

    show_btn_frame = ttk.Frame(show_todo,borderwidth=0, relief=SOLID, padding=[5, 5])

    def save():
        content_text = contentText.get(1.0, "end-1c")
        title_text = titleText.get(1.0, "end-1c")
        db.update_todo_by_id(row[0], content_text,title_text)
        showinfo(title="info", message=f"Заметка обновлена!")
        show_todo.destroy()



    save_button = tk.Button(show_btn_frame, text="Save", command=save)
    save_button.pack(anchor=E, padx=10, pady=10)

    def delete():
        db.delete_todo_by_id(row[0])
        showinfo(title="info", message=f"Заметка\n \"{title}\" \n удалена!")
        show_todo.destroy()

    del_button = tk.Button(show_btn_frame, text="Delete", command=delete)
    del_button.pack(anchor=E, padx=10, pady=10)

    show_btn_frame.pack(fill=X)

    show_todo.mainloop()
