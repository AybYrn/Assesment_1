import tkinter
import tkinter as tk
from tkinter import W, E
from PIL import Image, ImageTk
from GUI_Insert import GUI_Insert
import sqlite3


class Content_Gui:
    # @staticmethod
    # def fetch_db():
    #     connection = sqlite3.connect("./data/dishes.db")
    #     cursor = connection.cursor()
    #
    #     try:
    #         cursor.execute(
    #             "CREATE TABLE "
    #             "Dishes(NameOfDish, PostedBy, Ingredient, Instructions, numOfRates, AvgRate, Type, PhotoLocation)")
    #
    #         # Name of Dish, Who upload, Ingredient, Instructions, Number of rates, Avg rate, Type, photo

    #         cursor.executemany("INSERT INTO Dishes VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
    #         connection.commit()
    #     except:
    #         print("Dishes Table already exists")

    # def displayDishByName():

    # def displayAllDishes():

    # def displayDishByType():

    # def displayDishByRate():

    def __init__(self, master):
        self.master = master
        self.master.title("DISHES")
        bg_color = "#FF9AF6"

        # create a frame widget
        self.frame_2 = tk.Frame(self.master, width=500, height=250, bg="#BA8BFF")
        self.frame_2.pack(side=tk.TOP)
        self.frame_2.pack_propagate(False)
        from DishesData import data
        dishName_label = tk.Label(self.frame_2,
                                  text=data[0][0],
                                  width=30,
                                  bg="#BA8BFF",
                                  fg="#D74F00",
                                  font=("calibre", 15, "bold", "italic"))
        dishName_label.grid(row=0, column=0, columnspan=2, padx=35, pady=5)

        postedBy_label = tk.Label(self.frame_2,
                                  text=data[0][1],
                                  bg="#BA8BFF",
                                  fg="white",
                                  font=("calibre", 8, "bold"))
        postedBy_label.grid(row=1, column=0, padx=35)

        try:
            # create a frame 1 widgets
            print(data[4][7])
            new_img = Image.open("./assets/" + data[0][7])

            # Resize the image using resize() method
            resize_image = new_img.resize((160, 150))
            dish_img = ImageTk.PhotoImage(resize_image)

            logo_widget = tk.Label(self.frame_2, image=dish_img, bg="white")
            logo_widget.image = dish_img
            logo_widget.grid(row=2, column=0)
        except OSError:
            print("ValueError exception thrown")

        ings = data[0][2].split(" - ")
        res = ""

        for ing in ings:
            res += ing + "\n"

        ingredient_label = tk.Label(self.frame_2,
                                    text="-------- Ingredients --------\n" + res,
                                    bg="#BA8BFF",
                                    fg="white",
                                    font=("calibre", 10))
        ingredient_label.grid(row=2, column=1, padx=10)

        self.frame_3 = tk.Frame(self.frame_2, bg="#BA8BFF")
        self.frame_3.grid(row=3, column=0, columnspan=2)

        instruction_label = tk.Text(self.frame_3,
                                    height=10,
                                    width=50,
                                    bg="#BA8BFF",
                                    fg="white",
                                    state="normal",
                                    font=("calibre", 10))
        instruction_label.pack(side=tk.LEFT, padx=10, pady=5)

        scroll_bar = tkinter.Scrollbar(self.frame_3,
                                       orient="vertical",
                                       command=instruction_label.yview)
        # scroll_bar.set(10, 50)
        scroll_bar.pack(side=tk.LEFT, ipady=50)

        instruction_label["yscrollcommand"] = scroll_bar.set

        instruction_label.insert("1.0", data[3][3])
        instruction_label.configure(state="disabled")

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
                                font=("calibre", 10, "bold")
                                )
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
                                     # command=self.displayAllDishes
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
                                    # command=self.displayPrevious
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
                                # command=self.displayNext
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

    def pageInsert(self):
        self.frame_2.destroy()
        GUI_Insert(self.master)
