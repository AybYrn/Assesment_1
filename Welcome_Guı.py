import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
from Content_Gui import Content_Gui


def fetch_db():
    connection = sqlite3.connect("./data/dishes.db")
    cursor = connection.cursor()
    from DishesData import data

    try:
        cursor.execute("DROP TABLE DISHES")
        # Name of Dish, Who upload, Ingredient, Instructions, Number of rates, Avg rate, Type, photo
        cursor.execute(
            "CREATE TABLE "
            "Dishes(NameOfDish, PostedBy, Ingredient, Instructions, numOfRates, AvgRate, Type, PhotoLocation)")
        cursor.executemany("INSERT INTO Dishes VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        return connection
    except:
        print("Dishes Table already exists")


class Welcome_Gui:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("COOKING BOOK")
        bg_color = "#BA8BFF"

        # create a frame widget
        self.frame_1 = tk.Frame(self.master, width=500, height=500, bg=bg_color)
        self.frame_1.pack()
        self.frame_1.pack_propagate(False)

        try:
            # create a frame 1 widgets
            new_img = Image.open("assets/CookingBook.png")

            # Resize the image using resize() method
            resize_image = new_img.resize((150, 150))
            logo_img = ImageTk.PhotoImage(resize_image)

            logo_widget = tk.Label(self.frame_1, image=logo_img, bg=bg_color)
            logo_widget.image = logo_img
            logo_widget.pack(side=tk.TOP, pady=20)
        except OSError:
            print("ValueError exception thrown")

        tk.Label(self.frame_1,
                 text="Welcome\n To\n The Cooking Book",
                 bg=bg_color,
                 fg="#2B00FF",
                 font=("Helvetica", 20)).pack(side=tk.TOP, pady=15)

        continue_button = tk.Button(self.frame_1,
                                    text="CONTINUE >>",
                                    font=("Helvetica", 15),
                                    bg="white",
                                    fg="#2B00FF",
                                    cursor="hand2",
                                    activeforeground="#2B00FF",
                                    activebackground="#D7CEFF",
                                    command=lambda: self.pageContent())

        continue_button.pack(side=tk.TOP, pady=15)

        name = tk.Label(self.frame_1,
                        text="~ Aybuke Yaren ~",
                        font=("Helvetica", 15, "italic"),
                        bg=bg_color,
                        fg="#2B00FF"
                        )
        name.pack(side=tk.BOTTOM)

    def pageContent(self):
        self.frame_1.destroy()
        Content_Gui(self.master, fetch_db())


def main():
    root = tk.Tk()
    root.resizable(False, False)
    root.iconbitmap('./assets/favicon.ico')
    Welcome_Gui(root)
    root.mainloop()


main()
