from tkinter import*
import random
import time
import csv
from csv import writer
#import tkMessageBox
from tkinter import messagebox
from my_fusion import*
import sqlite3
conn = sqlite3.connect('my_database.db')

class Table:   
    def __init__(self,root): 
        # sample data 
        # lst = [(1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4),
        #     (1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4),
        #     (1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4),
        #     (1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4),
        #     (1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4),
        #     (1, 'Chernobyl', 'Drama', 7), 
        #     (2, 'How to ...','Drama', 6.7), 
        #     (3, 'The Truthful', 'Thriller', 5), 
        #     (4, 'Shutter Island', 'Drama', 3), 
        #     (5, 'Morocco', 'Drama', 4)] 
        # find total number of rows and columns in list 
        tree = FusionTree(243)
        f = open("moviess.csv", encoding="utf8")
        f.readline()
        # s = input("What are you inserting: ")
        # s = "Genre"
        length = 0
        for i in f:
            i = i.split(",")
            lst = [word.strip() for word in i]
            lst = [int(lst[0])] + lst[1:]
            print("lst", lst)
            self.tree.insert(lst)
            length += 1
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))                 
            self.entry.grid(row=length, column=0) 
            self.entry.insert(END, lst[0])
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=length, column=1) 
            self.entry.insert(END, lst[1])
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=length, column=2) 
            self.entry.insert(END, lst[2])
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=length, column=3) 
            self.entry.insert(END, lst[3])
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=length, column=4) 
            self.entry.insert(END, lst[4])
            
       
        f.close()
        self.tree.initiateTree()
        for i in range(10):
            print(i, "------------------->", self.tree.predecessor(i), sep = '\t')

        # self.total_rows = length 
        # self.total_columns = len(lst)

        # for creating table 
        # for i in range(self.total_rows):
        #         info_lst = tree.successor(i)                
        #         self.entry = Entry(root, width=26, fg='blue', 
        #                        font=('Arial',16,'bold'))                 
        #         self.entry.grid(row=i, column=0) 
        #         self.entry.insert(END, info_lst[0])
        #         self.entry.grid(row=i, column=1) 
        #         self.entry.insert(END, info_lst[1])
        #         self.entry.grid(row=i, column=2) 
        #         self.entry.insert(END, info_lst[2])
        #         self.entry.grid(row=i, column=3) 
        #         self.entry.insert(END, info_lst[3])
        #         self.entry.grid(row=i, column=4) 
        #         self.entry.insert(END, info_lst[4])

class Info:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1285x700+0+0")
        self.root.title("Movie Info")
        self.root.configure(bg='black')

        # display options
#         self.info_page_scroll = Scrollbar(self.root, bd=12, bg = 'black', orient=VERTICAL, width=20)
#         self.info_page_scroll.grid(row=0, column=4)

        self.display_area = Frame(self.root, width = 900, height=700, relief=SUNKEN, bg = 'black') # , yscrollcommand=self.info_page_scroll.set)
        self.display_area.grid(row=0, column=0)
        self.entry = Table(self.display_area)


        self.root.mainloop()

    def exit(self):
        self.root.destroy()

class Admin:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("Admin Page")
        self.root.configure(bg='black')

        # welcome label
        self.welcome = Label(self.root, font=( 'aria' ,25, 'bold' ),text="Welcome to admin page!",fg="white",bd=12,anchor='w', bg = 'black')
        self.welcome.place(x=50, y=0)

        # buttons
        self.add_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Add", bg="powder blue", command = self.add_movie)
        self.add_button.place(x=150,y=100)

        self.update_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Update", bg="powder blue", command = self.update_movie)
        self.update_button.place(x=150,y=200)

        self.delete_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Delete", bg="powder blue")
        self.delete_button.place(x=150,y=300)
        
        var1 = IntVar()
        FTrees = Checkbutton(master, text="Using Fusion Trees", variable=var1).place(x=400,y=230)
        Ftrees.config(font=('ariel' ,16,'bold'), bg='black', fg='white') 

        self.root.mainloop()
        
    def add_movie(self):
        self.root.destroy() #current window closed
        self.root = Tk() #new window
        self.user = add_details(self.root)
        
    def update_movie(self):
        self.root.destroy() #current window closed
        self.root = Tk() #new window
        self.user = update_details(self.root)
   
        
    def exit(self):
        self.root.destroy()
        
        
class update_details:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("Update existing movie entries")
        self.root.configure(bg='black')
        
        self.options = StringVar() #for drop down menu
        self.options.set("IMDB Rating")
        

        # buttons, inputs
        self.MovieName= StringVar()
        self.MovieDirector= StringVar()
        self.Genre = StringVar()
        self.ReleaseYear = StringVar()
        self.ReleaseDate= StringVar()
        self.IMDB_Rating= StringVar()
        
        

        self.lblMovieName = Label(self.root, font=( 'aria' ,16, 'bold' ),text= "Movie Name",fg="steel blue",bd=12,anchor='w', bg = 'black')
        self.lblMovieName.grid(row=2,column=2)
        self.txtMovieName = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieName , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieName.grid(row=2,column=3)

        self.lblMovieDirector = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Field to update",fg="steel blue",bd=10,anchor='w',bg = 'black')
        self.lblMovieDirector.grid(row=3,column=2)
        w = OptionMenu(self.root,self.options, "Movie Name", "MovieDirector", "Genre", "ReleaseYear", "ReleaseDate", "IMDB_Rating" )
        w.config(font=('ariel' ,16,'bold'),bg="powder blue",justify='left')
        w.grid(row=3,column=3)
#         self.txtMovieDirector= Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieDirector , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
#         self.txtMovieDirector.grid(row=1,column=3)
 
        self.lblGenre= Label(self.root, font=( 'aria' ,16, 'bold' ),text="New Value",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.lblGenre.grid(row=4,column=2)
        self.txtGenre = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.Genre , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtGenre.grid(row=4,column=3)



        self.root.mainloop()

    
    def exit(self):
        self.root.destroy()
        
    def enter_details(self):
        messagebox.showinfo("Message", "User has been successfully added")

class add_details:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("New Movie Entry details")
        self.root.configure(bg='black')

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

        self.show_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Add Details", bg="powder blue", command=self.enter_details)
        self.show_button.grid(row=6,column=3)

        self.root.mainloop()

    
    def exit(self):
        self.root.destroy()
        
    def enter_details(self):
        
        l =  list()
        l = [5, "Heello", "Horror", "6","2010"]
        
        with open('moviess.csv', 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(l)
                
        #t = table(self.root)
        
#         info = Toplevel()
#         self.movie_info = Info(info)
#         #entering deatils into the fusion tree
        #t = Table(self.root)

#         print("lll", l)
#         self.movie_info.insert(l)
#         for i in range(10):
#             print(i, "------------------->", tree.predecessor(i), sep = '\t')
#         #messagebox.showinfo("Message", "User has been successfully added")
#         
#         self.movie_info = Info(t)
    

class User:
    def __init__(self, master):
        self.root = master
        self.root.geometry("500x400+0+0")
        self.root.title("User Page")
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

        self.show_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Show", bg="powder blue", command=self.show_func)
        self.show_button.grid(row=6,column=3)

        self.root.mainloop()

    def show_func(self):
        info = Toplevel()
        self.movie_info = Info(info)

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
