from customtkinter import*

class App(CTk): # CTk() inheritance
    def __init__(self): # initialization magic function of class
        super().__init__()
        self.title("CustomTkinter Example") # setting a title of window
        self.geometry("320x470") # resolution of window
        self.resizable(False,False) # making window unable to resize
        self.create_widgets() # calling a function that we made to show a widgets

    def create_widgets(self): # create a widgets function
        CTkButton(self,text="I'm a Button", # creating a button
                  corner_radius=20).place(relx=.5,rely=.5,anchor='center')
        # place is aligning widget method, there's also pack() method but 
        # I'd rather to use this one


app = App() # creating an object
app.mainloop() # mainloop() is created for updating window every frame