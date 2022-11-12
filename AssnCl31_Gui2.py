

from tkinter import *



def displayDialog(window, movie_list):
    window2 = Toplevel(window)
    window2.geometry("1300x650")
    window2.title("Add Dialog")
    movieList = movie_list





#============================================================
# Event Handling Methods

    def displayAll():
        #text.insert(END, movieList[0][0])
        for i in range(0, len(movieList)):
            line=''+movieList[i][0]
            line+= '\t\t\t'+movieList[i][1]
            line+= '\t\t'+str(movieList[i][2])
            #line += '\t\tRating=' +str(movieList[i][3])
            line += '\t\tRating=' +str(movieList[i][4])
            line += '\t\t' +movieList[i][5]
            line += '\t\t' +movieList[i][7]
            netflix = movieList[i][6]
            if (netflix==True):
                line += '\t\t\tOn Netflix'


            line += '\n\n'
            text.insert(END, line)




    def closeEvent():
        window2.destroy()

    button6 = Button(window2, text="Close", fg="black", font=("arial", 12, "bold"), command=closeEvent)
    button6.place(x=10, y=10)

    text = Text(window2, undo=True, height=34, width=150)
    text.place(x=20, y=60)

    displayAll()














