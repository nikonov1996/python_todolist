import tkinter as tk
from tkinter import ttk, W, NO, VERTICAL, NW, N, SOLID, RIGHT, Y, X, E
from tkinter import END, BOTH

import db.todolist_db_provider as db
import models.config as gui_conf
from models.NewTODO import NewTODO
from models.ViewTODO import ViewTODO


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(gui_conf.title)
        self.geometry(gui_conf.size)
        self.s = ttk.Style()
        self.s.configure('height.Treeview',rowheight=40)
        self.frame = ttk.Frame(borderwidth=0, relief="raised",  padding=[0, 0])
        self.columns = ("id", "title", "date")
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings", cursor="hand2",style="height.Treeview")
        self.scrollbar = ttk.Scrollbar(self.frame,orient=VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side='right', fill=Y)

        self.tree.heading("id", text="№")
        self.tree.heading("title", text="Заголовок")
        self.tree.heading("date", text="Дата")
        self.tree.column("#1", stretch=NO, width=30)
        self.tree.column("#3", stretch=NO, width=120)
        # self.tree.bind('<ButtonRelease-1>',self.on_button_click())
        self.tree.pack(fill=X)
        self.tree["yscrollcommand"]=self.scrollbar.config().get('command')

        def item_selected(event):
            selected_people = ""
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                person = item["values"]
                selected_people = f"{selected_people}{person}\n"
            print(selected_people)
            self.view_todo_click(person[0])

        self.tree.bind("<<TreeviewSelect>>", item_selected)

        self.frame.pack( expand=True,fill=X)

        for row in db.get_todo_list():
            print(row)
            self.tree.insert("", END, values=(row[0],row[1],row[3]))

        self.btn_frame = ttk.Frame(borderwidth=0, relief=SOLID, padding=[5, 5])
        self.button = tk.Button(self.btn_frame, text="ADD", command=self.new_todo_click)
        self.button.pack(anchor=E, padx=10, pady= 10)
        self.btn_frame.pack(fill=X)

    def closeModal(self):
        self.destroy()

    def open(self):
        self.mainloop()

    def updateApp(self):
        self.closeModal()
        App().open()

    def view_todo_click(self, todo_id):
        result = db.get_todo_by_id(todo_id)
        ViewTODO(result,self).open()

    def new_todo_click(self):
        NewTODO(self).open()

