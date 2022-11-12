import tkinter as tk
from tkinter import W, E

from GUI_Insert import GUI_Insert
import sqlite3


class Content_Gui:

    @staticmethod
    def fetch_db():
        connection = sqlite3.connect("./data/dishes.db")
        cursor = connection.cursor()

        # Name of Dish, Who upload, Ingredient, Instructions, Number of rates, Avg rate, Type, photo
        data = [
            ("TChorizo & mozzarella gnocchi bake", "By Marianne Turner",
             "1 tbsp olive oil - 1 onion, finely chopped - 2 garlic cloves, crushed - 120g chorizo, diced - 2 x 400g "
             "cans chopped tomatoes - 1 tsp caster sugar - 600g fresh gnocchi - 125g mozzarella ball, cut into chunks "
             "- small bunch of basil, torn - green salad, to serve",
             "STEP 1 \nHeat the oil in a medium pan over a medium heat. Fry the onion and garlic for 8-10 mins until "
             "soft. Add the chorizo and fry for 5 mins more. Tip in the tomatoes and sugar, and season. Bring to a "
             "simmer, then add the gnocchi and cook for 8 mins, stirring often, until soft. Heat the grill to high. "
             "\nSTEP 2\nStir ¾ of the mozzarella and most of the basil through the gnocchi. Divide the mixture "
             "between six ovenproof ramekins, or put in one baking dish. Top with the remaining mozzarella, "
             "then grill for 3 mins, or until the cheese is melted and golden. Season, scatter over the remaining "
             "basil and serve with green salad.",
             483, 5, "Main", "./assets/gnocchi.png"),
            ("Easy chocolate fudge cake", "By Member recipe by misskay",
             "150ml sunflower oil, plus extra for the tin - 175g self-raising flour - 2 tbsp cocoa  - 1 tsp bicarbonate"
             "of soda - 150g caster sugar - 2 tbsp golden syrup - 2 large eggs, lightly beaten - 150ml semi-skimmed "
             "milk - 100g unsalted butter - 225g icing sugar - 40g cocoa powder - 2½ tbsp milk",
             "STEP 1\nHeat the oven to 180C/160C fan/gas 4. Oil and line the base of two 18cm sandwich tins. Sieve the"
             "flour, cocoa powder and bicarbonate of soda into a bowl. Add the caster sugar and mix well.\nSTEP "
             "2\nMake a well in the centre and add the golden syrup, eggs, sunflower oil and milk. Beat well with an"
             " electric whisk until smooth.\nSTEP 3\nPour the mixture into the two tins and bake for 25-30 mins until "
             "risen and firm to the touch. Remove from oven, leave to cool for 10 mins before turning out onto a"
             " cooling rack.\nSTEP 4\nTo make the icing, beat the unsalted butter in a bowl until soft. Gradually "
             "sieve and beat in the icing sugar and cocoa powder, then add enough of the milk to make the icing fluffy"
             " and spreadable.\nSTEP 5\nSandwich the two cakes together with the butter icing and cover the sides and"
             " the top of the cake with more icing.",
             939, 5, "Dessert", ".assets/fudgecake.png"),
            ("Pixie", "UK", 2021, 5, 3.1, "Comedy", True, "Drug Caper"),
            ("Martian", "US", 2015, 5, 4.6, "SciFi", False, "Spacetrip to Mars"),
            ("Grimbsy", "UK", 2016, 5, 3.6, "Comedy", True, "Action Comedy"),
            ("We're the Millers", "US", 2013, 5, 4.1, "Comedy", False, "Road Movie"),
            ("First Man", "US", 2018, 5, 4.1, "SciFi", True, "First Moon Landing"),
            ("Brian and Charles", "UK", 2022, 5, 3.1, "Comedy", False, "AI Robot Inventor"), ]

    #def displayDishByName():

    #def displayAllDishes():

    #def displayDishByType():

    #def displayDishByRate():

    def __init__(self, master):
        self.master = master
        self.master.title("DISHES")
        bg_color = "#FF9AF6"

        # create a frame widget
        self.frame_1 = tk.Frame(self.master, width=500, height=500, bg="#BA8BFF")
        self.frame_1.pack()
        self.frame_1.pack_propagate(False)

        searchName_button = tk.Button(self.frame_1,
                                      text="Display a Dish by Name",
                                      bg=bg_color,
                                      width=25,
                                      fg="white",
                                      font=("calibre", 10, "bold"),
                                      cursor="hand2",
                                      activeforeground="#2B00FF",
                                      activebackground="#D7CEFF",
                                      command=self.displayDishByName()
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
                                      command=self.displayDishByRate()
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
                                      command=self.displayDishByType()
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
                                     width=48,
                                     fg="white",
                                     cursor="hand2",
                                     activeforeground="#2B00FF",
                                     activebackground="#D7CEFF",
                                     command=self.displayAllDishes
                                     )
        searchAll_button.grid(row=3, columnspan=2, padx=20, sticky=W + E)

        insert_button = tk.Button(self.frame_1,
                                  text="Insert a Dish >>",
                                  font=("Helvetica", 10, "bold"),
                                  bg="white",
                                  fg="#2B00FF",
                                  cursor="hand2",
                                  activeforeground="#2B00FF",
                                  activebackground="#D7CEFF",
                                  command=lambda: self.pageInsert()
                                  )

        insert_button.grid(row=4, columnspan=2, padx=35, pady=20)

    def pageInsert(self):
        self.frame_1.destroy()
        GUI_Insert(self.master)
