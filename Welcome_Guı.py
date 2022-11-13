import tkinter as tk
from PIL import Image, ImageTk

from Content_Gui import Content_Gui


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
                 font=("Helvetica", 20, "bold")).pack(side=tk.TOP, pady=15)

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

    def pageContent(self):
        self.frame_1.destroy()
        Content_Gui(self.master)


def main():
    root = tk.Tk()
    Welcome_Gui(root)
    root.mainloop()


main()
