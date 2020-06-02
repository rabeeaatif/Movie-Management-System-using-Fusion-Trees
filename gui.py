from tkinter import*
import random
import time

class Admin:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1300x700+0+0")
        self.root.title("Movies Management System")
        self.root.configure(bg='grey')

        # buttons
        self.admin_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Admin", bg="powder blue")
        self.admin_button.place(x=150,y=250)

        self.root.mainloop()

    def exit(self):
        self.root.destroy()

class User:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("Movies Management System")
        self.root.configure(bg='grey')

        # buttons, inputs
        self.MovieName= StringVar()
        self.MovieDirector= StringVar()
        self.Genre = StringVar()
        self.ReleaseYear = StringVar()
        self.ReleaseDate= StringVar()
        self.IMDB_Rating= StringVar()


        self.lblMovieName = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Movie Name",fg="steel blue",bd=12,anchor='w', bg = 'black')
        self.lblMovieName.grid(row=0,column=2)
        self.txtMovieName = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieName , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieName.grid(row=0,column=3)

        self.lblMovieDirector = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Movie Director",fg="steel blue",bd=10,anchor='w',bg = 'black')
        self.lblMovieDirector.grid(row=1,column=2)
        self.txtMovieDirector= Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieDirector , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieDirector.grid(row=1,column=3)

        self.lblGenre= Label(self.root, font=( 'aria' ,16, 'bold' ),text="Genre",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.lblGenre.grid(row=2,column=2)
        self.txtGenre = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.Genre , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtGenre.grid(row=2,column=3)


        self.lblReleaseYear = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Release year",fg="steel blue",bd=10,anchor='w',  bg = 'black')
        self.lblReleaseYear.grid(row=3,column=2)
        self.txtReleaseYear = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.ReleaseYear , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtReleaseYear.grid(row=3,column=3)

        self.lblReleaseDate = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Release Date",fg="steel blue",bd=10,anchor='w',  bg = 'black')
        self.lblReleaseDate.grid(row=4,column=2)
        self.txtReleaseDate = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.ReleaseDate , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtReleaseDate.grid(row=4,column=3)

        self.lblIMDB_Rating = Label(self.root, font=( 'aria' ,16, 'bold' ),text="IMDB Rating",fg="steel blue",bd=10,anchor='w',  bg = 'black')
        self.lblIMDB_Rating.grid(row=5,column=2)
        self.txtIMDB_Rating = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.IMDB_Rating, bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtIMDB_Rating.grid(row=5,column=3)

        self.admin_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Show", bg="powder blue")
        self.admin_button.grid(row=6,column=3)

        self.root.mainloop()

    def exit(self):
        self.root.destroy()
        
class Start:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("Movies Management System")
        self.root.configure(bg='grey')

        # for heading, time display
        self.Tops = Frame(self.root,bg="black",width = 500,height=400,relief=SUNKEN)
        self.Tops.pack(side=TOP)

        localtime = time.asctime(time.localtime(time.time()))

        self.info = Label(self.Tops, font=( 'times' ,30, 'bold' ),text="Movies Management System",fg="white",bd=10,anchor='w', bg = 'black')
        self.info.grid(row=0,column=0)
        self.info = Label(self.Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W, bg = 'black')
        self.info.grid(row=1,column=0)

        # for user and admin buttons
        self.admin_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Admin", bg="powder blue", command=self.admin_button_func)
        self.admin_button.place(x=150,y=150)

        self.user_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="User", bg="powder blue", command=self.user_button_func)
        self.user_button.place(x=150,y=250)


        self.root.mainloop()
    
    def user_button_func(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = User(self.root)

    def admin_button_func(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Admin(self.root)

    def exit(self):
        self.root.destroy()

#-------------------------------------------
root = Tk()
s = Start(root)