
import sqlite3
from tkinter import *


from AssnCl31_Gui2 import *

window = Tk()
window.geometry("300x500")
window.title("Welcome")

#============================================================
# General Methods to Display Data

def displayChange():
    global current
    display(current)

def display(index):
    print('here')
    global current
    global product
    cur.execute("select * from Movie")
    currentMovie=cur.fetchall()[index]
    #print(currentMovie[0], currentMovie[1])
    current = index
    entry2.delete(0, END)
    entry2.insert(END, currentMovie[0])
    entry3.delete(0, END)
    entry3.insert(END, currentMovie[1])
    entry4.delete(0, END)
    entry4.insert(END, currentMovie[2])
    entry5a.delete(0, END)
    entry5a.insert(END, currentMovie[3])
    entry5.delete(0, END)
    entry5.insert(END, currentMovie[4])
    movieType = currentMovie[5]
    productTypeVar.set(movieType)
    onNetflix = currentMovie[6]
    if (onNetflix==True):
        var_cb1.set(1)
    else:
        var_cb1.set(0)
    entry7.delete(0, END)
    entry7.insert(END, currentMovie[7])




# End of Method Declarations
#========================================================================
# Database Setup
con = sqlite3.connect("../../Downloads/tutorial.db")
cur = con.cursor()
try:
    #cur.execute("DROP TABLE Movie")
    cur.execute("CREATE TABLE Movie(title,country, year,count, rating,genre, netflix,description)")
    data = [
        ("The Good Nurse", "US",2022,  5, 3.5, "Drama", True, "Murder Mystery"),
        ("Op Mincemeat", "UK", 2021,  5, 3.8, "Drama", False, "World War 2"),
        ("Pixie", "UK", 2021, 5, 3.1, "Comedy", True, "Drug Caper"),
        ("Martian", "US", 2015, 5, 4.6, "SciFi", False, "Spacetrip to Mars"),
        ("Grimbsy", "UK", 2016, 5, 3.6, "Comedy", True, "Action Comedy"),
        ("We're the Millers", "US", 2013, 5, 4.1, "Comedy", False, "Road Movie"),
        ("First Man", "US", 2018, 5, 4.1, "SciFi", True, "First Moon Landing"),
        ("Brian and Charles", "UK", 2022,  5, 3.1, "Comedy", False, "AI Robot Inventor"), ]

    cur.executemany("INSERT INTO Movie VALUES(?, ?, ?,?,?,?,?,?)", data)

    con.commit()

except:
    print("Movie Aready Exists")


#========= Definitions ============================




#-------Event Handling Methods ---------------

def cmdYearDisplay():
    year =yearTypeVar.get()
    cur.execute("select * from Movie where year = "+ str(year))
    #cur.execute("select * from Movie where year = " + '2022')
    yearMovies = cur.fetchall()
    displayDialog(window, yearMovies)

def cmdCategoryDisplay():
    category =catTypeVar.get()
    cur.execute("select * from Movie where genre = " + "\'"+ str(category) + "\'")
    genreMovies = cur.fetchall()
    displayDialog(window, genreMovies)

def deleteCurrentCmd():
    try:
        title=entry2.get()
        cur.execute("Delete from Movie where title = \'" + title + "\'")
        con.commit()
    except:
        print('Movie: ', title, ' does not exist in Database')




def updateRatingCmd():
    global current
    global product
    cur.execute("select * from Movie")
    currentMovie=cur.fetchall()[current]
    title=currentMovie[0]
    count=currentMovie[3]
    curr_rating=float(currentMovie[4])
    newRating = int(ratingTypeVar.get())

    cur.execute("Update Movie set count=count + 1 where title = \'"+title +"\'")
    newAverage = ( (count*curr_rating + newRating))/(count+1)
    newAverage = newAverage.__round__(3)
    cur.execute("Update Movie set rating=\'" + str(newAverage) + "\' where title = \'" + title + "\'")
    con.commit()
    display(current)

def nextCmd():
    global current
    cur.execute("select * from Movie")
    allMovies=cur.fetchall()
    if (current<(len(allMovies)-1) ):
        current += 1
        display(current)

def prevCmd():
    global current
    if (current > 0):
        current -= 1
        display(current)


# ----- Menu Event Handling -----------

def closeCmd():
    exit()



def clearCmd():
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry5a.delete(0, END)
    entry7.delete(0, END)
    entry5.insert(END, '0')
    entry5a.insert(END, '0')
    productTypeVar.set("Drama")
    var_cb1.set(0)

def insertCmd():
    title=entry2.get()
    country=entry3.get()
    year= int(entry4.get())
    count= 0
    rating= 0
    location=entry5.get()
    description1=entry7.get()
    onNetflix=False
    if  (var_cb1.get()==1):
        onNetflix=True
    newGenre = productTypeVar.get()
    newFilm = [

        (title, country, year,  0, 0, newGenre, onNetflix, description1), ]

    cur.executemany("INSERT INTO Movie VALUES(?, ?, ?,?,?,?,?,?)", newFilm)

    cur.execute("select * from Movie")
    allMovies=cur.fetchall()
    display(len(allMovies)-1)
    con.commit()

#-----------End of Event Handling


#=======================================================
# Menu to Add New Student
menu1 = Menu(window) #MenuBar
window.config(menu=menu1)
subm1=Menu(menu1)  #Menu
menu1.add_cascade(label="Admin", menu=subm1)
subm1.add_command(label="Delete Movie", font=("arial", 11, "bold"), command = deleteCurrentCmd)   # menu item
subm1.add_command(label="Close", font=("arial", 11, "bold"), command = closeCmd)

#======= End of Menu Definition ============================








frame = Frame(window, width=200, height=200)
frame.place(x=10,y=80)

label1 = Label(window, text="Movie Application", fg="blue",bg="yellow", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen


label2 = Label(frame, text="Title", fg="blue",width=15, font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '0')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Country", fg="blue",width=15, font=("arial", 10, "bold"))   #
label3.grid(row=1, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=1, column=1, sticky=W+E)

label4 = Label(frame, text="Year", fg="blue",width=15, font=("arial", 10, "bold"))   #
label4.grid(row=2, column=0, sticky=W+E)

entry4 = Entry(frame)
entry4.insert(END, '0')
entry4.grid(row=2, column=1, sticky=W+E)

label5a = Label(frame, text="# Ratings", fg="blue",width=15, font=("arial", 10, "bold"))   #
label5a.grid(row=3, column=0, sticky=W+E)

entry5a = Entry(frame)
entry5a.insert(END, '0')
entry5a.grid(row=3, column=1, sticky=W+E)


label5 = Label(frame, text="Avg Rating", fg="blue",width=15, font=("arial", 10, "bold"))   #
label5.grid(row=4, column=0, sticky=W+E)

entry5 = Entry(frame)
entry5.insert(END, '0')
entry5.grid(row=4, column=1, sticky=W+E)

label7 = Label(frame, text="Genre", fg="blue",width=15, font=("arial", 10, "bold"))   #
label7.grid(row=5, column=0, sticky=W+E)

list1=['Comedy','SciFi','Drama']
productTypeVar = StringVar()
combo1= OptionMenu(frame, productTypeVar, *list1)
productTypeVar.set("Comedy")
combo1.grid(row=5,column=1, sticky=W+E)


var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="On Netflix", variable=var_cb1)
cb1.grid(row=6,column=0,columnspan=2)
#---------------------------

entry7 = Entry(frame)
entry7.insert(END, '')
entry7.grid(row=7, column=0, columnspan=2, sticky=W+E)

labelBlank = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank.grid(row=10, column=0, columnspan=2,sticky=W+E)

button5 = Button(frame, text="Next", fg="black", font=("arial", 10, "bold"), command=nextCmd)
button5.grid(row=11, column=0, sticky=W+E)

button6 = Button(frame, text="Prev", fg="black", font=("arial", 10, "bold"), command=prevCmd)
button6.grid(row=11, column=1, sticky=W+E)

button7 = Button(frame, text="Clear", fg="black", font=("arial", 10, "bold"), command=clearCmd)
button7.grid(row=12, column=0, sticky=W+E)

button8 = Button(frame, text="InsertItem", fg="black", font=("arial", 10, "bold"), command=insertCmd)
button8.grid(row=12, column=1, sticky=W+E)

button11 = Button(frame, text="Add Rating", fg="black", font=("arial", 10, "bold"), command=updateRatingCmd)
button11.grid(row=15, column=0, sticky=W+E)

list11=['1','2','3','4','5']
ratingTypeVar = StringVar()
combo11= OptionMenu(frame, ratingTypeVar, *list11)
ratingTypeVar.set("3")
combo11.grid(row=15,column=1, sticky=W+E)

labelBlank2 = Label(frame, text=" ", fg="blue",width=15, font=("arial", 10, "bold"))   #
labelBlank2.grid(row=16, column=0, columnspan=2,sticky=W+E)


cur.execute("select * from Movie")
allMovies = cur.fetchall()
button12 = Button(frame, text="Display All Movies", fg="black", font=("arial", 10, "bold"), command=lambda : displayDialog(window, allMovies))
button12.grid(row=17, column=0, columnspan=2, sticky=W+E)

button12 = Button(frame, text="Display By Year", fg="black", font=("arial", 10, "bold"), command=cmdYearDisplay)
button12.grid(row=18, column=0, columnspan=1, sticky=W+E)

yearTypeVar = StringVar()
list12=[2022,2021,2020,2019,2018,2017,2016,2015]
combo12= OptionMenu(frame, yearTypeVar, *list12)
yearTypeVar.set(2022)
combo12.grid(row=18,column=1, sticky=W+E)

button13 = Button(frame, text="Display By Category", fg="black", font=("arial", 10, "bold"), command=cmdCategoryDisplay)
button13.grid(row=19, column=0, columnspan=1, sticky=W+E)

catTypeVar = StringVar()
list13=['Drama', 'Comedy', 'SciFi']
combo13= OptionMenu(frame, catTypeVar, *list13)
catTypeVar.set('Drama')
combo13.grid(row=19,column=1, sticky=W+E)




display(0)









mainloop()




