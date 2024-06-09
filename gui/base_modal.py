import tkinter as tk
from tkinter import ttk, W, NO, VERTICAL, NW, N, SOLID, RIGHT, Y, X, E
from tkinter import END, BOTH


import db.todolist_db_provider as db
import gui.config as gui_conf
import gui.show_todo as showModal


main = tk.Tk()

def on_button_click():
    print("Hello, Tkinter!")

def show_todo_click(id):
    result = db.get_todo_by_id(id)
    main.destroy()
    showModal.drowModal(result)


def drawTodoListFrame():
    s = ttk.Style()
    s.configure('height.Treeview',rowheight=40)
    frame = ttk.Frame(borderwidth=0, relief="raised",  padding=[0, 0])
    columns = ("id", "title", "date")
    tree = ttk.Treeview(frame, columns=columns, show="headings", cursor="hand2",style="height.Treeview")
    scrollbar = ttk.Scrollbar(frame,orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side='right', fill=Y)

    tree.heading("id", text="№")
    tree.heading("title", text="Заголовок")
    tree.heading("date", text="Дата")
    tree.column("#1", stretch=NO, width=30)
    tree.column("#3", stretch=NO, width=100)
    tree.bind('<ButtonRelease-1>',on_button_click())
    tree.pack(fill=X)
    tree["yscrollcommand"]=scrollbar.config().get('command')

    def item_selected(event):
        selected_people = ""
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            person = item["values"]
            selected_people = f"{selected_people}{person}\n"
        print(selected_people)
        show_todo_click(person[0])

    tree.bind("<<TreeviewSelect>>", item_selected)

    frame.pack( expand=True,fill=X)

    for row in db.get_todo_list():
        print(row)
        tree.insert("", END, values=(row[0],row[1],row[3]))


def drawBtnFrame():
    btn_frame = ttk.Frame(borderwidth=0, relief=SOLID, padding=[5, 5])
    button = tk.Button(btn_frame, text="ADD", command=on_button_click)
    button.pack(anchor=E, padx=10, pady= 10)
    btn_frame.pack(fill=X)

def drowMain():
    main.title(gui_conf.title)
    main.geometry(gui_conf.size)
    drawTodoListFrame()
    drawBtnFrame()
    main.mainloop()

drowMain()