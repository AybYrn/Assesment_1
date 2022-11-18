import tkinter as tk
from PIL import Image, ImageTk

bg_color = "#BA8BFF"


class DisplayDishes:
    def __init__(self, master: tk.Tk, disharr):
        self.disharr = disharr
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
        self.display()

    def display(self):
        self.frame_2.children.clear()
        for index, dish in enumerate(self.disharr[
                                     (self.page - 1) * self.page_dish_count:
                                     ((self.page - 1) * self.page_dish_count + self.page_dish_count)
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

        next_button = tk.Button(self.frame_2,
                                text="Next >>",
                                font=("Helvetica", 10, "bold"),
                                bg=bg_color,
                                fg="white",
                                cursor="hand2",
                                activeforeground="#2B00FF",
                                activebackground="#D7CEFF",
                                command=self.nextpagecmd
                                )
        next_button.grid(row=self.page_dish_count + 1, columnspan=2)

    def nextpagecmd(self):
        self.page = self.page + 1
        self.display()
