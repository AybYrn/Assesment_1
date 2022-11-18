import tkinter
import tkinter as tk
from sqlite3 import Connection
from tkinter import W, E
from PIL import Image, ImageTk

from Display_dishes import DisplayDishes
from GUI_Insert import GUI_Insert
import sqlite3


class Content_Gui:

    # def displayDishByName():

    # def displayDishByType():
    #
    # def displayDishByRate():

    def __init__(self, master, connection: Connection, current_dish=0):
        self.master = master
        self.connection = connection
        self.current_dish = current_dish

        def displayAllDishes():
            cursor = connection.cursor()
            res = cursor.execute("SELECT * FROM DISHES")
            self.frame_2.destroy()
            DisplayDishes(self.master, res.fetchall())

        self.master.title("DISHES")
        bg_color = "#FF9AF6"

        # create a frame widget
        self.frame_2 = tk.Frame(self.master, bg="#BA8BFF")
        self.frame_2.pack(side=tk.TOP)
        self.frame_2.pack_propagate(False)

        from DishesData import data
        self.data = data

        self.dishName_label = tk.Label(self.frame_2,
                                       width=30,
                                       height=3,
                                       wraplength=300,
                                       bg="#BA8BFF",
                                       fg="#D74F00",
                                       font=("calibre", 15, "bold", "italic"))
        self.dishName_label.grid(row=0, column=0, columnspan=2, padx=35)

        self.postedBy_label = tk.Label(self.frame_2,
                                       bg="#BA8BFF",
                                       fg="white",
                                       wraplength=100,
                                       height=3,
                                       font=("calibre", 9, "bold"))
        self.postedBy_label.grid(row=1, column=0, padx=35)

        self.logo_widget = tk.Label(self.frame_2, bg="white")
        self.logo_widget.grid(row=2, column=0, padx=15)

        self.ingredient_label = tk.Label(self.frame_2,
                                         bg="#BA8BFF",
                                         fg="white",
                                         width=40,
                                         wraplength=250,
                                         font=("calibre", 10))
        self.ingredient_label.grid(row=2, column=1, padx=5)

        self.frame_3 = tk.Frame(self.frame_2, bg="#BA8BFF")
        self.frame_3.grid(row=3, column=0, columnspan=2)

        self.instruction_label = tk.Text(self.frame_3,
                                         height=10,
                                         width=60,
                                         bg="#BA8BFF",
                                         fg="white",
                                         font=("calibre", 10))
        self.instruction_label.pack(side=tk.LEFT, padx=10, pady=5)

        scroll_bar = tkinter.Scrollbar(self.frame_3,
                                       orient="vertical",
                                       command=self.instruction_label.yview)
        # scroll_bar.set(10, 50)
        scroll_bar.pack(side=tk.LEFT, ipady=50)

        self.instruction_label["yscrollcommand"] = scroll_bar.set

        # create a frame widget
        self.frame_1 = tk.Frame(self.frame_2, width=500, height=500, bg="#BA8BFF")
        self.frame_1.grid(row=4, column=0, columnspan=2)

        searchName_button = tk.Button(self.frame_1,
                                      text="Display a Dish by Name",
                                      bg=bg_color,
                                      width=25,
                                      fg="white",
                                      font=("calibre", 10, "bold"),
                                      cursor="hand2",
                                      activeforeground="#2B00FF",
                                      activebackground="#D7CEFF",
                                      # command=self.displayDishByName()
                                      )
        searchName_button.grid(row=0, column=0, padx=10, pady=5)

        search_entry = tk.Entry(self.frame_1,
                                bg="white",
                                font=("calibre", 10, "bold"))
        search_entry.grid(row=0, column=1, padx=10, pady=5)

        searchRate_button = tk.Button(self.frame_1,
                                      text="Display a Dish by Rate >>",
                                      font=("Helvetica", 10, "bold"),
                                      bg=bg_color,
                                      width=25,
                                      fg="white",
                                      cursor="hand2",
                                      activeforeground="#2B00FF",
                                      activebackground="#D7CEFF",
                                      # command=self.displayDishByRate()
                                      )
        searchRate_button.grid(row=1, column=0, padx=10, pady=5)

        rating = ['1', '2', '3', '4', '5']
        rateTypeVar = tk.StringVar()
        rateTypeVar.set("Choose a rate!")
        cb1 = tk.OptionMenu(self.frame_1, rateTypeVar, *rating)
        cb1.config(bg="#FF9AF6", fg="white", width=16, cursor="hand2", )
        cb1["menu"].config(bg="#FF9AF6")
        cb1.grid(row=1, column=1, padx=10, pady=5)

        searchRate_button = tk.Button(self.frame_1,
                                      text="Display a Dish by Type",
                                      font=("Helvetica", 10, "bold"),
                                      bg=bg_color,
                                      width=25,
                                      fg="white",
                                      cursor="hand2",
                                      activeforeground="#2B00FF",
                                      activebackground="#D7CEFF",
                                      # command=self.displayDishByType()
                                      )
        searchRate_button.grid(row=2, column=0, padx=10, pady=5)

        rating = ['Dessert', 'Starter', 'Main', 'Drink', 'Side']
        rateTypeVar = tk.StringVar()
        rateTypeVar.set("Choose a Type!")
        cb1 = tk.OptionMenu(self.frame_1, rateTypeVar, *rating)
        cb1.config(bg="#FF9AF6", fg="white", width=16, cursor="hand2", )
        cb1["menu"].config(bg="#FF9AF6")
        cb1.grid(row=2, column=1, padx=10, pady=5)

        searchAll_button = tk.Button(self.frame_1,
                                     text="Display All Dish",
                                     font=("Helvetica", 10, "bold"),
                                     bg=bg_color,
                                     width=49,
                                     fg="white",
                                     cursor="hand2",
                                     activeforeground="#2B00FF",
                                     activebackground="#D7CEFF",
                                     command=displayAllDishes
                                     )
        searchAll_button.grid(row=3, columnspan=2, padx=20, sticky=W + E)

        self.frame_4 = tk.Frame(self.frame_2, bg="#BA8BFF")
        self.frame_4.grid(row=5, column=0, columnspan=2, padx=35)

        previous_button = tk.Button(self.frame_4,
                                    text="<< Previous",
                                    font=("Helvetica", 10, "bold"),
                                    bg=bg_color,
                                    fg="white",
                                    cursor="hand2",
                                    activeforeground="#2B00FF",
                                    activebackground="#D7CEFF",
                                    command=self.displayPrevious
                                    )
        previous_button.pack(side=tk.LEFT, pady=15)

        next_button = tk.Button(self.frame_4,
                                text="Next >>",
                                font=("Helvetica", 10, "bold"),
                                bg=bg_color,
                                fg="white",
                                cursor="hand2",
                                activeforeground="#2B00FF",
                                activebackground="#D7CEFF",
                                command=self.displayNext
                                )
        next_button.pack(side=tk.LEFT)

        insert_button = tk.Button(self.frame_4,
                                  text="Insert a Dish >>",
                                  font=("Helvetica", 10, "bold"),
                                  bg="white",
                                  fg="#2B00FF",
                                  cursor="hand2",
                                  activeforeground="#2B00FF",
                                  activebackground="#D7CEFF",
                                  command=lambda: self.pageInsert()
                                  )

        insert_button.pack(side=tk.LEFT, padx=35, pady=20)

        self.updateDishes()

    def displayPrevious(self):
        if self.current_dish > 0:
            self.current_dish -= 1
            self.updateDishes()

    def displayNext(self):
        number_of_data = len(self.data)
        if self.current_dish < number_of_data - 1:
            self.current_dish += 1
            self.updateDishes()

    def updateDishes(self):
        self.dishName_label.config(
            text=self.data[self.current_dish][0]
        )
        self.postedBy_label.config(
            text=self.data[self.current_dish][1]
        )

        ingredients = self.data[self.current_dish][2].split(" - ")
        res = ""
        for ing in ingredients:
            res += "\n" + ing

        self.ingredient_label.config(
            text="-------- Ingredients --------" + res
        )

        self.instruction_label.configure(state="normal")
        self.instruction_label.delete("1.0", tk.END)
        self.instruction_label.insert(
            "1.0", self.data[self.current_dish][3]
        )
        self.instruction_label.configure(state="disabled")

        try:
            # create a frame 1 widgets
            new_img = Image.open("./assets/" + self.data[self.current_dish][7])

            # Resize the image using resize() method
            resize_image = new_img.resize((160, 150))

            dish_img = ImageTk.PhotoImage(resize_image)

            self.logo_widget.configure(image=dish_img)
            self.logo_widget.image = dish_img
        except OSError:
            print("Picture Not Found ın the Assets folder")

    def pageInsert(self):
        self.frame_2.destroy()
        GUI_Insert(self.master, self.connection)
