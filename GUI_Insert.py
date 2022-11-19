import os
import shutil
import tkinter as tk
from sqlite3 import Connection
from tkinter import W, E, WORD
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


class GUI_Insert:
    def __init__(self, master, connection: Connection):
        self.master = master
        self.connection = connection
        self.filename = None
        self.master.title("INSERT A DISH TO THE BOOK")
        bg_color = "#BA8BFF"

        self.frame_2 = tk.Frame(self.master, width=600, height=600, bg=bg_color)
        self.frame_2.grid(row=0, column=0)
        self.frame_2.pack_propagate(False)

        title_label = tk.Label(self.frame_2,
                               text="Enter a title:",
                               width=10,
                               bg=bg_color,
                               fg="white",
                               font=("calibre", 10, "bold"))
        title_label.grid(row=1, column=0, padx=35, pady=5)

        self.title_entry = tk.Text(self.frame_2,
                                   width=30,
                                   height=5,
                                   wrap=WORD,
                                   bg="white",
                                   font=("calibre", 10, "bold"))
        self.title_entry.grid(row=1, column=1, pady=5)

        ingredient_label = tk.Label(self.frame_2,
                                    text="Enter ingredients:",
                                    bg=bg_color,
                                    fg="white",
                                    font=("calibre", 10, "bold"))
        ingredient_label.grid(row=2, column=0, padx=35, pady=5)

        self.ingredient_text = tk.Text(self.frame_2,
                                       width=30,
                                       height=10,
                                       wrap=WORD,
                                       bg="white",
                                       font=("calibre", 10, "bold"))
        self.ingredient_text.grid(row=2, column=1, padx=35, pady=5)

        instruction_label = tk.Label(self.frame_2,
                                     text="Enter instruction:",
                                     bg=bg_color,
                                     fg="white",
                                     font=("calibre", 10, "bold"))
        instruction_label.grid(row=3, column=0, padx=35, pady=5)

        self.instruction_text = tk.Text(self.frame_2,
                                        width=30,
                                        wrap=WORD,
                                        height=15,
                                        bg="white",
                                        font=("calibre", 10, "bold"))
        self.instruction_text.grid(row=3, column=1, padx=35, pady=5)

        rating_label = tk.Label(self.frame_2,
                                text="Enter a rate:",
                                bg=bg_color,
                                fg="white",
                                font=("calibre", 10, "bold"))
        rating_label.grid(row=4, column=0, padx=35, pady=5)

        rating = ['1', '2', '3', '4', '5']
        self.rateTypeVar = tk.StringVar()
        self.rateTypeVar.set("Choose a rate!")
        cb1 = tk.OptionMenu(self.frame_2, self.rateTypeVar, *rating)
        cb1.config(bg="#282FFF", fg="white", width=16)
        cb1["menu"].config(bg="#282FFF")
        cb1.grid(row=4, column=1, padx=35, pady=5)

        name_label = tk.Label(self.frame_2,
                              text="Enter your name:",
                              bg=bg_color,
                              fg="white",
                              font=("calibre", 10, "bold"))
        name_label.grid(row=6, column=0, padx=35, pady=5)

        self.name_entry = tk.Entry(self.frame_2,
                                   bg="white",
                                   font=("calibre", 10, "bold"))
        self.name_entry.grid(row=6, column=1)

        type_label = tk.Label(self.frame_2,
                              text="Enter type of dish:",
                              bg=bg_color,
                              fg="white",
                              font=("Helvetica", 10, "bold"))
        type_label.grid(row=7, column=0, padx=35, pady=5)

        typeOfDish = ['Dessert', 'Starter', 'Main', 'Side', 'Drinks']
        self.productTypeVar = tk.StringVar()
        self.productTypeVar.set("Choose a type!")
        cb1 = tk.OptionMenu(self.frame_2, self.productTypeVar, *typeOfDish)
        cb1.config(bg="#282FFF", fg="white", width=16)
        cb1["menu"].config(bg="#282FFF")
        cb1.grid(row=7, column=1, padx=35, pady=5)

        upload_button = tk.Button(self.frame_2,
                                  text="Upload a Photo",
                                  font=("Helvetica", 10, "bold"),
                                  bg="white",
                                  fg="#282FFF",
                                  cursor="hand2",
                                  activeforeground="#282FFF",
                                  activebackground="white",
                                  command=lambda: upload_photo())
        upload_button.grid(row=8, column=0, padx=35, pady=5)

        add_button = tk.Button(self.frame_2,
                               text="ADD",
                               font=("Helvetica", 10, "bold"),
                               bg="white",
                               fg="#282FFF",
                               cursor="hand2",
                               activeforeground="#282FFF",
                               activebackground="white",
                               command=self.pageContent)
        add_button.grid(row=9, columnspan=2, padx=35, pady=5)

        def upload_photo():
            global img
            f_types = [('Jpeg', '*.jpeg'), ('Png', '*png'), ('Jpg', '*.jpg')]
            self.filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(self.filename)
            img_resized = img.resize((150, 100))  # new width & height
            img = ImageTk.PhotoImage(img_resized)
            b2 = tk.Button(self.frame_2, image=img)  # using Button
            b2.grid(row=8, column=1, padx=35, pady=5)

    def insertDish(self):
        name = str(self.title_entry.get("1.0", "end-1c").strip())
        provider = str(self.name_entry.get())
        ingredients = str(self.ingredient_text.get("1.0", "end-1c"))
        instructions = str(self.instruction_text.get("1.0", "end-1c"))
        numofrates = str(1)
        producttype = str(self.productTypeVar.get())
        avgrate = str(self.rateTypeVar.get())
        pic = str(self.filename)

        if not (len(name) == 0 or len(provider) == 0 or len(ingredients) == 0 or len(instructions) == 0
                or avgrate == "Choose a rate!" or producttype == "Choose a type!" or len(pic) == 0):
            pic_arr = pic.split("/")
            pic_name = pic_arr[len(pic_arr) - 1]
            shutil.copy(pic, "./assets/" + pic_name)

            newDish = [
                name, provider, ingredients, instructions, numofrates, avgrate, producttype, pic_name
            ]
            cursor = self.connection.cursor()
            res = cursor.execute("INSERT INTO DISHES VALUES(?, ?, ?, ?, ?, ?, ?, ?)", newDish)
            self.connection.commit()
            return True
        else:
            print("Fill The Empty Area !!")

    def pageContent(self):
        if self.insertDish():
            from Content_Gui import Content_Gui
            self.frame_2.destroy()
            Content_Gui(self.master, self.connection)
