from tkinter import*
import random
import time
#import tkMessageBox
from tkinter import messagebox
from fusion_tree import*

class Table:   
    def __init__(self,root, tree, genre, movie, year, f_tree_length):
        self.tree = tree
        final_lst = []
        
        for i in range(1, f_tree_length):
            lst = self.tree.successor(i)
            if len(final_lst) > 0:
                if lst != final_lst[-1]:
                    if movie != "":
                        if genre != "" and genre != "Select":
                            if year != "":
                                if lst[1] == movie and lst[2] == genre and lst[4] == year:
                                    final_lst.append(lst)
                            elif lst[1] == movie and lst[2] == genre:
                                final_lst.append(lst)
                        elif lst[1] == movie and lst[4] == year:
                            final_lst.append(lst)
                        elif lst[1] == movie:
                            final_lst.append(lst)
                    elif genre != "" and genre != "Select":
                        if year != "":
                            if lst[2] == genre and lst[4] == year:
                                final_lst.append(lst)
                        elif lst[2] == genre:
                            final_lst.append(lst)
                    elif year != "":
                        if lst[4] == year:
                            final_lst.append(lst)
            else:
                if movie != "":
                    if genre != "" and genre != "Select":
                        if year != "":
                            if lst[1] == movie and lst[2] == genre and lst[4] == year:
                                final_lst.append(lst)
                        elif lst[1] == movie and lst[2] == genre:
                            final_lst.append(lst)
                    elif lst[1] == movie and lst[4] == year:
                        final_lst.append(lst)
                    elif lst[1] == movie:
                        final_lst.append(lst)
                elif genre != "" and genre != "Select":
                    if year != "":
                        if lst[4] == year and lst[2] == genre:
                            final_lst.append(lst)
                    elif lst[2] == genre:
                        final_lst.append(lst)
                elif year != "":
                    if lst[4] == year:
                        final_lst.append(lst)

        self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))                 
        self.entry.grid(row=0, column=0) 
        self.entry.insert(END, "Movie Id")
        self.entry.config(state=DISABLED)
        
        self.entry = Entry(root, width=26, fg='blue', 
                            font=('Arial',16,'bold'))
        self.entry.grid(row=0, column=1) 
        self.entry.insert(END, "Movie Name")
        self.entry.config(state=DISABLED)
        
        self.entry = Entry(root, width=26, fg='blue', 
                            font=('Arial',16,'bold'))
        self.entry.grid(row=0, column=2) 
        self.entry.insert(END, "Genres")
        self.entry.config(state=DISABLED)
        
        self.entry = Entry(root, width=26, fg='blue', 
                            font=('Arial',16,'bold'))
        self.entry.grid(row=0, column=3) 
        self.entry.insert(END, "IMDb Rating")
        self.entry.config(state=DISABLED)
        
        self.entry = Entry(root, width=26, fg='blue', 
                            font=('Arial',16,'bold'))
        self.entry.grid(row=0, column=4) 
        self.entry.insert(END, "Year")
        self.entry.config(state=DISABLED)
            

        for i in range(len(final_lst)):
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))                 
            self.entry.grid(row=i+1, column=0) 
            self.entry.insert(END, final_lst[i][0])
            self.entry.config(state=DISABLED)
            
            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=i+1, column=1) 
            self.entry.insert(END, final_lst[i][1])
            self.entry.config(state=DISABLED)

            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=i+1, column=2) 
            self.entry.insert(END, final_lst[i][2])
            self.entry.config(state=DISABLED)

            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=i+1, column=3) 
            self.entry.insert(END, final_lst[i][3])
            self.entry.config(state=DISABLED)

            self.entry = Entry(root, width=26, fg='blue', 
                               font=('Arial',16,'bold'))
            self.entry.grid(row=i+1, column=4) 
            self.entry.insert(END, final_lst[i][4])
            self.entry.config(state=DISABLED)

class Info:
    def __init__(self, master, tree, genre, movie, year, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 1600//2
        y = screen_height//2 - 700//2

        self.root.geometry("1600x700+%d+%d" % (x, y))
        self.root.title("Movie Info")
        self.root.configure(bg='black')

        self.tree = tree
        self.tree_length = f_tree_length
        self.genre = genre
        self.movie = movie
        self.year = year

        # display options
        self.info_page_scroll = Scrollbar(self.root, bd=12, bg = 'black', orient=VERTICAL, width=20)
        self.info_page_scroll.grid(row=0, column=5)

        self.display_area = Frame(self.root, width = 900, height=700, relief=SUNKEN, bg = 'black')#, yscrollcommand=self.info_page_scroll.set)
        self.display_area.grid(row=0, column=0)
        self.entry = Table(self.display_area, self.tree, self.genre, self.movie, self.year, self.tree_length)

        self.root.mainloop()

    def exit(self):
        self.root.destroy()

class Admin:
    def __init__(self, master, tree, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 500//2
        y = screen_height//2 - 400//2

        self.root.geometry("500x400+%d+%d" % (x, y))
        self.root.title("Admin Page")
        self.root.configure(bg='black')

        self.tree = tree
        self.tree_length = f_tree_length

        # welcome label
        self.welcome = Label(self.root, font=( 'aria' ,25, 'bold' ),text="Welcome to admin page!",fg="white",bd=12,anchor='w', bg = 'black')
        self.welcome.place(x=50, y=0)

        # buttons
        self.add_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Add", bg="powder blue", command = self.add_movie)
        self.add_button.place(x=150,y=100)

        self.update_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Update", bg="powder blue", command = self.update_movie)
        self.update_button.place(x=150,y=170)

        self.delete_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Delete", bg="powder blue")
        self.delete_button.place(x=150,y=240)

        self.back_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Back", bg="powder blue", command=self.back_start)
        self.back_button.place(x=150,y=310)

        self.root.mainloop()
        
    def add_movie(self):
        self.root.destroy() #current window closed
        self.root = Tk() #new window
        self.user = add_details(self.root, self.tree, self.tree_length)
        
    def update_movie(self):
        self.root.destroy() #current window closed
        self.root = Tk() #new window
        self.user = update_details(self.root, self.tree, self.tree_length)

    def back_start(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Start(self.root, self.tree, self.tree_length)

    def exit(self):
        self.root.destroy()
        
        
class update_details:
    def __init__(self, master, tree, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 500//2
        y = screen_height//2 - 400//2

        self.root.geometry("500x400+%d+%d" % (x, y))
        self.root.title("Update existing movie entries")
        self.root.configure(bg='black')
        
        self.tree = tree
        self.tree_length = f_tree_length

        self.options = StringVar() #for drop down menu
        self.options.set("Select")
        
        # buttons, inputs
        self.MovieName= StringVar()
        self.Changed_value = StringVar()
        

        self.lblMovieId = Label(self.root, font=( 'aria' ,16, 'bold' ),text= "Movie Name",fg="steel blue",bd=12,anchor='w', bg = 'black')
        self.lblMovieId.grid(row=2,column=2)
        self.txtMovieId = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieName , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieId.grid(row=2,column=3)

        self.lblMovieName = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Field to update",fg="steel blue",bd=10,anchor='w',bg = 'black')
        self.lblMovieName.grid(row=3,column=2)
        w = OptionMenu(self.root,self.options, "Movie Name", "Genre", "Release Year", "IMDB Rating" )
        w.config(font=('ariel' ,16,'bold'),bg="powder blue",justify='left')
        w.grid(row=3,column=3)
 
        self.Changed_value = Label(self.root, font=( 'aria' ,16, 'bold' ),text="New Value",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.Changed_value.grid(row=4,column=2)
        self.txtchanged = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.Changed_value , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtchanged.grid(row=4,column=3)

        self.add_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Update", bg="powder blue", command=self.enter_details)
        self.add_button.grid(row=6,column=3)

        self.back_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Back", bg="powder blue", command=self.back_admin)
        self.back_button.grid(row=7,column=3)

        self.root.mainloop()

    
    def exit(self):
        self.root.destroy()
        
    def enter_details(self):
        messagebox.showinfo("Message", "Information has been successfully added")

    def back_admin(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Admin(self.root, self.tree, self.tree_length)

class add_details:
    def __init__(self, master, tree, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 500//2
        y = screen_height//2 - 400//2

        self.root.geometry("500x400+%d+%d" % (x, y))
        self.root.title("New Movie Entry details")
        self.root.configure(bg='black')

        self.tree = tree
        self.tree_length = f_tree_length

        # buttons, inputs
        self.MovieId = IntVar()
        self.MovieName = StringVar()
        self.Genre = StringVar()
        self.ReleaseYear = StringVar()
        self.ReleaseDate = StringVar()
        self.IMDB_Rating = StringVar()


        self.lblMovieId = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Movie Id",fg="steel blue",bd=12,anchor='w', bg = 'black')
        self.lblMovieId.grid(row=0,column=2)
        self.txtMovieId = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieId , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieId.grid(row=0,column=3)

        self.lblMovieName = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Movie Name",fg="steel blue",bd=10,anchor='w',bg = 'black')
        self.lblMovieName.grid(row=1,column=2)
        self.txtMovieName= Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.MovieName , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtMovieName.grid(row=1,column=3)

        self.lblGenre= Label(self.root, font=( 'aria' ,16, 'bold' ),text="Genre",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.lblGenre.grid(row=2,column=2)
        self.txtGenre = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.Genre , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtGenre.grid(row=2,column=3)


        self.lblReleaseYear = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Release year",fg="steel blue",bd=10,anchor='w',  bg = 'black')
        self.lblReleaseYear.grid(row=3,column=2)
        self.txtReleaseYear = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.ReleaseYear , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtReleaseYear.grid(row=3,column=3)


        self.lblIMDB_Rating = Label(self.root, font=( 'aria' ,16, 'bold' ),text="IMDB Rating",fg="steel blue",bd=10,anchor='w',  bg = 'black')
        self.lblIMDB_Rating.grid(row=4,column=2)
        self.txtIMDB_Rating = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.IMDB_Rating, bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.txtIMDB_Rating.grid(row=4,column=3)

        self.add_button = Button(self.root, padx=16, pady=8, bd=4, fg="black", font=('ariel' ,16,'bold'), width=10, text="Add Details", bg="powder blue", command=self.enter_details)
        self.add_button.grid(row=5,column=3)

        self.back_button = Button(self.root, padx=16, pady=8, bd=4, fg="black", font=('ariel' ,16,'bold'), width=10, text="Back", bg="powder blue", command=self.back_admin)
        self.back_button.grid(row=6,column=3)

        self.root.mainloop()

    
    def exit(self):
        self.root.destroy()
        
    def enter_details(self):
        lst = [(self.MovieId).get(), self.MovieName.get(), self.Genre.get(), self.IMDB_Rating.get(), self.ReleaseYear.get()]
        flag = True
        for i in range(0, len(lst)):
            if i == 0:
                if lst[i] == 0:
                    flag = False
                    messagebox.showinfo("Message", "Please enter Movie Id!")
                    break
            elif len(lst[i]) == 0:
                messagebox.showinfo("Message", "Please enter all the informations!")
                flag = False
                break
        if flag:
            self.tree.insert(lst)
            messagebox.showinfo("Message", "Information has been successfully added!")

    def back_admin(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Admin(self.root, self.tree, self.tree_length)


class User:
    def __init__(self, master, tree, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 500//2
        y = screen_height//2 - 400//2

        self.root.geometry("500x400+%d+%d" % (x, y))
        self.root.title("User Page")
        self.root.configure(bg='grey')

        self.tree = tree
        self.tree_length = f_tree_length

        # buttons, inputs
        self.options = StringVar() #for drop down menu
        self.options.set("Select")
        self.movie = StringVar()
        self.year = StringVar()
        
        self.genre = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Genre",fg="steel blue",bd=10,anchor='w',bg = 'black')
        self.genre.grid(row=3,column=2)

        self.label_genre = OptionMenu(self.root,self.options, "Comedy", "Action", "Adventure", "Crime", "Mystery", "Animation")
        self.label_genre.config(font=('ariel' ,16,'bold'),bg="powder blue",justify='left')
        self.label_genre.grid(row=3,column=3)

        self.enter_movie = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Movie Name",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.enter_movie.grid(row=4,column=2)
        self.movie_entered = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.movie , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.movie_entered.grid(row=4,column=3)

        self.enter_year = Label(self.root, font=( 'aria' ,16, 'bold' ),text="Year Released",fg="steel blue",bd=10,anchor='w', bg = 'black')
        self.enter_year.grid(row=5,column=2)
        self.movie_year = Entry(self.root,font=('ariel' ,16,'bold'), textvariable=self.year , bd=6,insertwidth=4,bg="powder blue" ,justify='left')
        self.movie_year.grid(row=5,column=3)


        self.search_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Search", bg="powder blue", command=self.search)
        self.search_button.grid(row=6,column=3)

        self.back_button = Button(self.root, padx=16, pady=8, bd=10, fg="black", font=('ariel' ,16,'bold'), width=10, text="Back", bg="powder blue", command=self.back_user)
        self.back_button.grid(row=7,column=3)

        self.root.mainloop()

    def search(self): # search by
        info = Toplevel()
        self.movie_info = Info(info, self.tree, self.options.get(), self.movie.get(), self.year.get(), self.tree_length)

    def back_user(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Start(self.root, self.tree, self.tree_length)

    def exit(self):
        self.root.destroy()
        
class Start:
    def __init__(self, master, tree, f_tree_length):
        self.root = master
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = screen_width//2 - 500//2
        y = screen_height//2 - 400//2

        self.root.geometry("500x400+%d+%d" % (x, y))
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

        # initiate f-tree
        self.tree = tree
        self.tree_length = f_tree_length

        self.root.mainloop()
    
    def user_button_func(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = User(self.root, self.tree, self.tree_length)

    def admin_button_func(self):
        self.root.destroy() # current window closed
        self.root = Tk() #new window
        self.user = Admin(self.root, self.tree, self.tree_length)

    def exit(self):
        self.root.destroy()

#-------------------------------------------
if __name__ == "__main__":
    # create a fusion tree of degree 3
    tree = FusionTree(243)
    f = open("movies.csv", encoding="utf8")
    f.readline()
    f_tree_length = 0
    for i in f:
        i = i.split(",")
        lst = [word.strip() for word in i]
        lst = [int(lst[0])] + lst[1:]
        tree.insert(lst)
        f_tree_length += 1
    f.close()
    print(f_tree_length)
    tree.initiateTree()
    # gui
    root = Tk()
    s = Start(root, tree, f_tree_length)
    