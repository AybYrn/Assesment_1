import tkinter as tk
from tkinter import W, E
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


class GUI_Insert:
    def __init__(self, master):
        self.master = master
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
        title_label.grid(row=1, column=0, padx=35, pady=20)

        title_entry = tk.Entry(self.frame_2,
                               width=16,
                               bg="white",
                               font=("calibre", 10, "bold"))
        title_entry.grid(row=1, column=1)

        ingredient_label = tk.Label(self.frame_2,
                                    text="Enter ingredients:",
                                    bg=bg_color,
                                    fg="white",
                                    font=("calibre", 10, "bold"))
        ingredient_label.grid(row=2, column=0, padx=35, pady=20)

        ingredient_text = tk.Text(self.frame_2,
                                  width=20,
                                  height=5,
                                  bg="white",
                                  font=("calibre", 10, "bold"))
        ingredient_text.grid(row=2, column=1, padx=35, pady=20)

        instruction_label = tk.Label(self.frame_2,
                                     text="Enter instruction:",
                                     bg=bg_color,
                                     fg="white",
                                     font=("calibre", 10, "bold"))
        instruction_label.grid(row=3, column=0, padx=35, pady=20)

        instruction_text = tk.Text(self.frame_2,
                                   width=20,
                                   height=5,
                                   bg="white",
                                   font=("calibre", 10, "bold"))
        instruction_text.grid(row=3, column=1, padx=35, pady=20)

        rating_label = tk.Label(self.frame_2,
                                text="Enter a rate:",
                                bg=bg_color,
                                fg="white",
                                font=("calibre", 10, "bold"))
        rating_label.grid(row=4, column=0, padx=35, pady=20)

        rating = ['1', '2', '3', '4', '5']
        rateTypeVar = tk.StringVar()
        rateTypeVar.set("Choose a rate!")
        cb1 = tk.OptionMenu(self.frame_2, rateTypeVar, *rating)
        cb1.config(bg="#282FFF", fg="white", width=16)
        cb1["menu"].config(bg="#282FFF")
        cb1.grid(row=4, column=1, padx=35, pady=20)

        name_label = tk.Label(self.frame_2,
                              text="Enter your name:",
                              bg=bg_color,
                              fg="white",
                              font=("calibre", 10, "bold"))
        name_label.grid(row=6, column=0, padx=35, pady=20)

        name_entry = tk.Entry(self.frame_2,
                              bg="white",
                              font=("calibre", 10, "bold"))
        name_entry.grid(row=6, column=1)

        type_label = tk.Label(self.frame_2,
                              text="Enter type of dish:",
                              bg=bg_color,
                              fg="white",
                              font=("Helvetica", 10, "bold"))
        type_label.grid(row=7, column=0, padx=35, pady=20)

        typeOfDish = ['Dessert', 'Starter', 'Main', 'Side', 'Drinks']
        productTypeVar = tk.StringVar()
        productTypeVar.set("Choose a type!")
        cb1 = tk.OptionMenu(self.frame_2, productTypeVar, *typeOfDish)
        cb1.config(bg="#282FFF", fg="white", width=16)
        cb1["menu"].config(bg="#282FFF")
        cb1.grid(row=7, column=1, padx=35, pady=20)

        upload_button = tk.Button(self.frame_2,
                                  text="Upload a Photo",
                                  font=("Helvetica", 10, "bold"),
                                  bg="white",
                                  fg="#282FFF",
                                  cursor="hand2",
                                  activeforeground="#282FFF",
                                  activebackground="white",
                                  command=lambda: upload_photo())
        upload_button.grid(row=8, column=0, padx=35, pady=20)

        add_button = tk.Button(self.frame_2,
                               text="ADD",
                               font=("Helvetica", 10, "bold"),
                               bg="white",
                               fg="#282FFF",
                               cursor="hand2",
                               activeforeground="#282FFF",
                               activebackground="white",
                               command= self.pageContent)
        add_button.grid(row=9, columnspan=2, padx=35, pady=20)

        def upload_photo():
            global img
            f_types = [('Jpeg', '*.jpeg'), ('Png', '*png'), ('Jpg', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            img_resized = img.resize((150, 100))  # new width & height
            img = ImageTk.PhotoImage(img_resized)
            b2 = tk.Button(self.frame_2, image=img)  # using Button
            b2.grid(row=8, column=1, padx=35, pady=20)

    def pageContent(self):
        from Content_Gui import Content_Gui
        self.frame_2.destroy()
        Content_Gui(self.master)
