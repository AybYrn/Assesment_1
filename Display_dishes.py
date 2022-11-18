import tkinter as tk
from sqlite3 import Connection

from PIL import Image, ImageTk

bg_color = "#BA8BFF"


class DisplayDishes:
    def __init__(self, master: tk.Tk, disharr, connction: Connection):
        self.disharr = disharr
        self.connection = connction
        self.page = 1
        self.page_dish_count = 5
        self.master = master
        self.master.title("DISHES")

        # create a frame widget
        self.frame_1 = tk.Frame(self.master, bg=bg_color)
        self.frame_1.pack()
        self.frame_1.pack_propagate(False)

        self.frame_2 = tk.Frame(self.frame_1, bg=bg_color)
        self.frame_2.grid(row=0, column=0)

        self.frame_3 = tk.Frame(self.frame_1, bg=bg_color)
        self.frame_3.grid(row=self.page_dish_count + 1, columnspan=2)

        self.display()

    def display(self):
        self.frame_2.destroy()
        self.frame_2 = tk.Frame(self.frame_1, bg=bg_color)
        self.frame_2.grid(row=0, column=0)

        last = (self.page - 1) * self.page_dish_count + self.page_dish_count
        for index, dish in enumerate(self.disharr[
                                     (self.page - 1) * self.page_dish_count:last
                                     ]):
            # create a frame 1 widgets
            new_img = Image.open("./assets/" + dish[7])

            # Resize the image using resize() method
            resize_image = new_img.resize((100, 90))

            dish_img = ImageTk.PhotoImage(resize_image)

            logo_widget = tk.Label(self.frame_2, image=dish_img, bg=bg_color)
            logo_widget.image = dish_img
            logo_widget.grid(row=index, column=0, padx=10)

            dishName_label = tk.Label(self.frame_2,
                                      text=dish[0] + "\n# of Rate: " + str(
                                          dish[5]) + "\nAverage rate: " + str(dish[6]),
                                      width=40,
                                      wraplength=350,
                                      anchor="w",
                                      bg="#BA8BFF",
                                      fg="black",
                                      font=("calibre", 9, "bold", "bold"))
            dishName_label.grid(row=index, column=1, padx=5)

        prev_button = tk.Button(self.frame_3,
                                text="<< Previous",
                                font=("Helvetica", 10, "bold"),
                                bg=bg_color,
                                fg="white",
                                cursor="hand2",
                                activeforeground="#2B00FF",
                                activebackground="#D7CEFF",
                                command=self.prevpagecmd
                                )
        prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        next_button = tk.Button(self.frame_3,
                                text="Next >>",
                                font=("Helvetica", 10, "bold"),
                                bg=bg_color,
                                fg="white",
                                cursor="hand2",
                                activeforeground="#2B00FF",
                                activebackground="#D7CEFF",
                                command=self.nextpagecmd
                                )
        next_button.pack(side=tk.LEFT)

        return_button = tk.Button(self.frame_3,
                                  text="Go Back",
                                  font=("Helvetica", 10, "bold"),
                                  bg="white",
                                  fg="#282FFF",
                                  cursor="hand2",
                                  activeforeground="#282FFF",
                                  activebackground="white",
                                  command=self.pageContent)
        return_button.pack(side=tk.LEFT, padx=10)

    def prevpagecmd(self):
        if self.page > 1:
            self.page -= 1
            self.display()

    def nextpagecmd(self):
        if self.page < len(self.disharr) / self.page_dish_count:
            self.page += 1
            self.display()

    def pageContent(self):
        from Content_Gui import Content_Gui
        self.frame_1.destroy()
        Content_Gui(self.master, self.connection)
