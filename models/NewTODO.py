import tkinter as tk
from tkinter import ttk, W, NO, VERTICAL, NW, N, SOLID, RIGHT, Y, X, E, S
from tkinter import END, BOTH
from tkinter.messagebox import showinfo
import db.todolist_db_provider as db
import models.config as gui_conf
from models import *


class NewTODO(tk.Tk):

    def __init__(self, app):
        super().__init__()
        self.geometry(gui_conf.size)
        self.title(gui_conf.title)

        self.content_todo_frame = ttk.Frame(self, borderwidth=0, relief=SOLID, padding=[5, 5])

        self.titleText = tk.Text(self.content_todo_frame, wrap="word")
        self.titleText.configure(height=1)
        self.titleText.pack(fill=X)
        self.contentText = tk.Text(self.content_todo_frame, wrap="word")
        self.contentText.configure(height=15)
        self.contentText.pack(fill=X)

        self.content_todo_frame.pack(fill=BOTH, expand=True)

        self.show_btn_frame = ttk.Frame(self, borderwidth=0, relief=SOLID, padding=[5, 5])

        def save():
            content_text = self.contentText.get(1.0, "end-1c")
            title_text = self.titleText.get(1.0, "end-1c")
            db.add_new_todo( title_text, content_text)
            self.closeModal()
            showinfo(title="info", message=f"Заметка создана успешно!")
            app.updateApp()

        self.save_button = tk.Button(self.show_btn_frame, text="Save", command=save)
        self.save_button.pack(anchor=E, padx=10, pady=10)

        self.show_btn_frame.pack(fill=X)

    def closeModal(self):
        self.destroy()

    def open(self):
        self.mainloop()
