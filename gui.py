from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Movies Management System")
root.configure(bg='black')

Tops = Frame(root,bg="black",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN, bg = 'black')
f1.pack(side=LEFT)

# f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
# f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'times' ,30, 'bold' ),text="Movies Management System",fg="white",bd=10,anchor='w', bg = 'black')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W, bg = 'black')
lblinfo.grid(row=1,column=0)

text_Input=StringVar()
operator =""


def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""


def qexit():
    root.destroy()

#---------------------------------------------------------------------------------------
MovieName= StringVar()
MovieDirector= StringVar()
Genre = StringVar()
ReleaseYear = StringVar()
ReleaseDate= StringVar()
IMDB_Rating= StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Movie Name",fg="steel blue",bd=12,anchor='w', bg = 'black')
lblreference.grid(row=0,column=2)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=MovieName , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
txtreference.grid(row=0,column=3)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Movie Director",fg="steel blue",bd=10,anchor='w',bg = 'black')
lblfries.grid(row=1,column=2)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=MovieDirector , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=3)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Genre",fg="steel blue",bd=10,anchor='w', bg = 'black')
lblLargefries.grid(row=2,column=2)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Genre , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=3)

lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Release year",fg="steel blue",bd=10,anchor='w',  bg = 'black')
lblburger.grid(row=3,column=2)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=ReleaseYear , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=3)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Release Date",fg="steel blue",bd=10,anchor='w',  bg = 'black')
lblFilet.grid(row=4,column=2)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=ReleaseDate , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtFilet.grid(row=4,column=3)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="IMDB Rating",fg="steel blue",bd=10,anchor='w',  bg = 'black')
lblCheese_burger.grid(row=5,column=2)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=IMDB_Rating, bd=6,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="show", bg="powder blue")
btnexit.grid(row=7, column=3)


root.mainloop()

