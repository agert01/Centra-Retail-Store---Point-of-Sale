"""

Name:           Agert Berisha
Student:        X00175572
Date:           21/04/2022

Description:
Python GUI Development Project - Centra Retail Store

"""


import tkinter as tk


def Centra_Login():
    #executes when trying to log into the account
    
    
    # opens text files in read mode
    NewUsername = open("NewUsername.txt","r")
    readUsername = NewUsername.read()
    NewPassword = open("NewPassword.txt","r")
    readPassword = NewPassword.read()
    
    
    # if username and password entered in the entry boxes match the text in the text files than it will succesfully login
    if (Username.get() == Read_Username or Username.get() == readUsername)  and (Password.get() == Read_Password or Password.get() == readPassword):
        
        # print text
        print("Succesful login")
        #removes grids if login is successful
        Centra.grid_remove()
        Label01.grid_remove()
        UsernameLabel.grid_remove()
        UsernameEntry.grid_remove()
        PasswordLabel.grid_remove()
        PasswordEntry.grid_remove()
        LoginButton.grid_remove()
        
        
        # adding a menu
        menuBar = tk.Menu(r)
        r.config(menu=menuBar)
        SubMenu1 = tk.Menu(menuBar,tearoff=0)
        SubMenu2 = tk.Menu(menuBar,tearoff=0)
        
        #add menus to the menu
        
        # Shopping menu linked to SubMenu1 "Food Shopping" that when pressed command is Food_Shopping
        menuBar.add_cascade(label="Shopping",
                            menu=SubMenu1,
                            command=Food_Shopping)
        
        # Contact menu linked to SubMenu2 "Contact us" that when pressed command is ContactSection
        menuBar.add_cascade(label="Contact",
                            menu=SubMenu2)
        
        # add submenus of the menu
        SubMenu1.add_command(label="Food Shopping",
                             command=Food_Shopping)
        SubMenu2.add_command(label="Contact Us",
                             command=ContactSection)
        
        #reassign root window size
        r.geometry("1100x675")
        #remove grid
        CreateNewAccount.grid_remove()
        
        
        # display canvas
        LoginCanvas.grid(row=1,column=1)
        #creates an image in the canvas with SouthEast anchor and CentraBG image and height and width
        LoginCanvas.create_image(1100,675,anchor="se",image=CentraBg)
        
        # create a rectangle in the canvas being used to display a similar centra logo
        LoginCanvas.create_rectangle(10,30,300,140,fill="blue")
        # create text in the canvas that is positioned inside the rectangle, filled with orange
        # font Times 20 italic bold
        LoginCanvas.create_text(150,65,fill="orange",font="Times 20 italic bold",
                                text="CENTRA")
        # create text in canvas positioned inside the rectangle under the previous text,
        # filled with white and font is Times 20 italic bold underline
        LoginCanvas.create_text(150,100,fill="white",font="Times 20 italic bold underline",
                                text="Brighten up your day")
        # created text in canvas than is on after the rectangle on the right stating a title with Bold font and size 17, filled with red color
        LoginCanvas.create_text(700,100,fill="red",text=CentraTitle,font=("Bold",17))
        # centra mission text created in canvas with custom color and Helvetica font size 14
        LoginCanvas.create_text(260,400,fill="#3A4F31",text=CentraMission,font=("Helvetica",14))
        
        
    elif Username.get() != Read_Username or Password.get() != Read_Password:
        print("Try again")
    
      
    
def ContactSection():
    #removes grids
    LoginButton.grid_remove()
    LoginCanvas.grid_remove()
    TopSellersFrame.grid_remove()
    RSFrame.grid_remove()
    
    #reassign root window size
    r.geometry("450x600")
    
    # configures frame with new height and width and green background
    ContactFrame.config(height=600,width=500,bg="green")
    #display at row 1 and column 2
    ContactFrame.grid(row=1,column=1)
    # configure label with new text and font, size 13
    SelectLabel.config(text="Select which staff of our Centra would u like to contact",
                       font =("Italic Bold",13))
    SelectLabel.place(x=10,y=10) # will appear at these co-ordinates in the frame
    
    # configures manager checkbutton with variable t, and onvalue=1,offvalue=0
    # yellow background and Arial font with size 20
    # command is displayInfo when pressed
    Manager.config(text="Manager: David Cruise",
                   variable = t,
                   onvalue=1,
                   offvalue=0,
                   command=displayInfo,
                   bg="yellow",
                   font=("Arial",20))
    # will appear at these co-ordinates in the frame 
    Manager.place(x=10,y=60)
    
    # confugres supervisor checkbuttons with variable s, onvalue=1,offvalue=0
    # yellow background and ariall font with size 20
    # command is displayInfo when pressed
    Supervisor.config(text="Supervisor: Agert Berisha",
                      variable = s,
                      onvalue=1,
                      offvalue=0,
                      command=displayInfo,
                      bg="yellow",
                      font=("Arial",20))
    # will appear at these co-ordinates in the frame 
    Supervisor.place(x=10,y=250)
    
    
    
    

def displayInfo():
    
    # if t value is 1 display manager info
    if (t.get() ==1):
        # displays text details with Roman times font size 10 in a light blue background
        manager_info.config(text="Phone: 083 333 3333\nEmail: davidcruise01@gmail.com\nAddress: Centra Greenpark, Clondalkin,Dublin",
                            font =("Roman Times",10),
                            bg="light blue")
        manager_info.place(x=10,y=130)# will appear at these co-ordinates in the frame 
    
    
    # if s value is 1, displays supervisor info
    if (s.get()==1):
        # displays text details with Roman Times font size 10 in a light blue background
       supervisor_info.config(text="Phone: 083 123 3211\nEmail: agertb01@gmail.com\nAddress: Centra Greenpark, Clondalkin,Dublin",
                            font =("Roman Times",10),
                            bg="light blue")
       supervisor_info.place(x=10,y=350) # will appear at these co-ordinates in the frame 
    
    
        

    
    
    
    
                            

def Food_Shopping():
    
    # remove grids from tkinter window
    ContactFrame.grid_remove()
    SliderFrame.grid_remove()
    LoginCanvas.grid_remove()
    
    #reassign root window size
    r.geometry("1100x675")
    # reconfigure background of root window
    r.configure(bg="silver")
    # reconfigures frame with green background
    TopSellersFrame.configure(bg="green")
    
    
    
    # calls global variables
    global ImageCounter
    global FoodImage
    global name
    global price
    
    
    
    
    #for loops with 4 variables to access 4-dimensional arrays
    #needed 4 variables otherwise I would get error that it wouldn't unpack 
    
    
   # loop creates 5 Radiobuttons on the left Side column 1
   # more efficient than writing every radiobutton one by one
   # Radiobutton has parrent window TopSellersFrame, text is the name variable
   # image is FoodImage , value is price and command is addPrice
    for ImageCounter, FoodImage, name, price in Items_left:
        
        FoodImage = tk.Radiobutton(TopSellersFrame,text=name,
                                   compound="top",
                                   image=FoodImage,
                                   variable = v,
                                   value = price,
                                   indicatoron="false",
                                   command=addPrice)
        
        
        # column 1 radiobuttons
        FoodImage.grid(row=ImageCounter,column=1)
    
    for ImageCounter, FoodImage, name, price in Items_left01:
        
        FoodImage = tk.Radiobutton(TopSellersFrame,text=name,
                                   compound="top",
                                   image=FoodImage,
                                   variable = v,
                                   value = price,
                                   indicatoron="false",                               
                                   command=addPrice)
        
        #column 2 radiobuttons
        FoodImage.grid(row=ImageCounter,column=2)
    
    for ImageCounter, FoodImage, name, price in Items_right:
          
          FoodImage = tk.Radiobutton(TopSellersFrame,text=name,
                                     compound="top",
                                     image=FoodImage,
                                     variable = v,
                                     value = price,
                                     indicatoron="false",
                                     command=addPrice)
        
          #column 3 radiobuttons
          FoodImage.grid(row=ImageCounter,column=3)
    
    
    for ImageCounter, FoodImage, name, price in Items_right01:
          
          FoodImage = tk.Radiobutton(TopSellersFrame,text=name,
                                     compound="top",
                                     image=FoodImage,
                                     variable = v,
                                     value = price,
                                     indicatoron="false",
                                     command=addPrice)
        
          #column 4 radiobuttons
          FoodImage.grid(row=ImageCounter,column=4)
    
    # reconfigures frame with light blue background and height,width
    RSFrame.config(bg="light blue",height=675,width=600)
    
    # configures label with parent window root, silver background and width 20
    space_label=tk.Label(r,bg="silver",width=20)
    # displays at assigned row and column with sticky NORTH
    space_label.grid(row=1,column=5,sticky=tk.N)
    
    # will appear at these co-ordinates in the frame or root window
    Search_label.place(x=40,y=10)
    Search_item.place(x=220,y=13)
    Search_button.place(x=410,y=10)
    total_price_topSellers.place(x=350,y=630)
    Finish.place(x=10,y=630)
    
    
    
    # displays at assigned row and column 
    TopSellersFrame.grid(row=1,column=1)
    RSFrame.grid(row=1,column=2)
    
    
    
def AddtoBasket():
    # add the tempPrice value in the AllPrices array
    AllPrices.append(tempPrice)
    #print in console window
    print(AllPrices)

def addPrice():
    #executed when selecting radiobutton items in the shopping section
    
    # call global variables
    global x1
    global y1
    global nameArray
    
    #x1 runs through names, y1 runs through prices 
    for x1 , y1 in Items_on_stock:
        # if radiobutton value is equal to a price value y1 in item_on_stock array it executes
        if float(v.get()) == y1:
            # reconfigures message to display name of item and its price, message has width of 400
            M2.config(text = x1 +" has price of: "+str(y1)+" €" +" and it has been added to basket",
                               width=400)
            M2.place(x = 50,y =350) # will appear at these co-ordinates in the frame
            # adds the name of this item in the nameArray
            nameArray.append(x1)
            #print the array of names in the console window
            print(nameArray)
       
    # adds the price of that item that was selected in the AllPrices array    
    AllPrices.append(v.get())
    
    #prints total price in console window
    print("Current prices in basket are: " + str(AllPrices))
    
    

def NewAccount_Display():
    #executed when trying to create a new account to log-in
    
    # reconfigure label
    Label01.configure(text="Please enter new account details")
    # reconfigure username and password label
    UsernameLabel.configure(text="Create New Username*")
    PasswordLabel.configure(text="Create New Password*")
    
    #remove login and createnewaccount button grid
    LoginButton.grid_remove()
    CreateNewAccount.grid_remove()
    
    
    
    # reconfigure button with silver background and command that brings user back to log-in area when pressed
    CA.configure(text="Create Account",
                 bg = "silver",
                 command = Back_To_Login)
    # displays button at specified row and grid with sticky NORTH
    CA.grid(row=9,column=1,sticky=tk.N)
    
                               
   
def Back_To_Login():
    # this is executed after creating a new account and going back to log-in area
   
    # open text file in write mode
    NewUsername = open("NewUsername.txt","w")
    # writes the string username entered in the username entry box
    NewUsername.write(Username.get())
    #close file
    NewUsername.close()
    
    # open file in write mode
    NewPassword = open("NewPassword.txt","w")
    # write the news string password entered in the entry box 
    NewPassword.write(Password.get())
    #close file
    NewPassword.close()
    
    #reconfigures label
    Label01.configure(text="Please enter details below to login")
    #reconfigures username label
    UsernameLabel.configure(text="Username*")
    #reconfigures username label
    PasswordLabel.configure(text="Password*")
    # removes create account button
    CA.grid_remove()
    
    # displays a new loggin button with command Centra_Login if pressed
    # blue background and yellow text foreground
    LoginButton = tk.Button(r,text="Login",
                        bg="blue",
                        fg="yellow",
                        command=Centra_Login)
    #display button at specified row and column with sticky NORTH
    LoginButton.grid(row=7,column=1,sticky=tk.N)
    
    
    
def SearchItem():
    #calls global variable
    global tempPrice
    
    # reconfigures message widget that displays text
    m1.config(text = "Nothing has been searched and/or  is not available yet")
    m1.place(x=40,y=50) # will appear at these co-ordinates in the frame
    
    # productName runs through the names, productPrice runs through the prices in the Items_on_Stock array
    for productName,productPrice in Items_on_stock:
        # if string inside search entry box is equal to a product name executes
        if Search.get() == productName:
            # reconfigures message widget to display product name and its price
            m1.config(text=productName+" is available and it's price is: "+str(productPrice)+" euro")
            # moves the product price to tempPrice
            tempPrice = productPrice
            #add the product name that was searched into the nameArray, later used to display all the item names selected
            nameArray.append(productName) 
            m1.place(x=40,y=50) # will appear at these co-ordinates in the frame
            Add_to_Basket.place(x = 380,y=50) # will appear at these co-ordinates in the frame
      
    # prints the temporary price in console window
    print(tempPrice)
            
    
def TotalPrice():
    
    #call global variables
    global tempPrice
    global Sum_of_Prices
    global x1
    global nameArray
    
    #runs through the AllPrices array
    for x in AllPrices:
        # adds each element of the array into Sum_of_Prices variable one at a time
        Sum_of_Prices = x + Sum_of_Prices
    # created a new variable that stores the Sum_Of_prices float value with a max of 2 decimal values 
    summ = float("{0:.2f}".format(Sum_of_Prices))
    # reconfigures message widget to display all the names of items selected and their total price
    #relief raised makes it stick out a bit more, looking more proffesional, custom background, width 450
    # so even if the message is long it kinda stays in 1 line 
    totalMessage.config(text="Total items added are:" + str(nameArray) + " with final price of "+str(summ)+" €",
                       width=450,bg="#B2C13A",relief="raised")  # raised makes the message stick out more
    totalMessage.place(x=10,y=500)# will appear at these co-ordinates in the frame
    
    
    # refreshes these variables
    Sum_of_Prices = 0
    tempPrice = 0
  

  
def Finish():
    
    # removes these frames
    TopSellersFrame.grid_remove()
    RSFrame.grid_remove()
    
    # new root window size
    r.geometry("500x600")
    #configures SliderFrame with height, width and light blue background
    SliderFrame.config(height=600,width=500,bg="light blue")
    SliderFrame.grid(row=1,column=1)
    Slider.place(x=175,y=60) # will appear at these co-ordinates in the frame
    
    # label widget with parent window SliderFrame, displayed as text in Arial font size 10
    review = tk.Label(SliderFrame,text="How happy were you from 0 to 100 with the service?",
                      font=("Arial",10))
    review.place(x=100,y=30) # will appear at these co-ordinates in the frame
    
    # Rating Button with yellow background and submit_rating command when pressed, parent window is Slider Frame
    # yellow background
    RatingButton = tk.Button(SliderFrame,text="Submit Rating",
                             bg="yellow",
                             command=Submit_Rating)
    RatingButton.place(x=185,y=110) # will appear at these co-ordinates in the frame
    
    
    # label widget in SliderFrame with parent window SliderFrame, displays text in Arial font size 10
    textlabel=tk.Label(SliderFrame,
                       text="Please, could you provide extra feedback on how we could improve our service?",
                       font=("Arial",10))
    textlabel.place(x=25,y=220) # will appear at these co-ordinates in the frame
    
    # reconfigures text area with white background and height and width
    text_area.config(bg="white",height=15,width=50) 
    text_area.place(x=40,y=250) # will appear at these co-ordinates in the frame
    textArea_Button.place(x=170,y=500)  # will appear at these co-ordinates in the frame
    # binds the root to escape button, when this button pressed the CloseApplication command is executed
    r.bind("<Escape>",CloseApplication)

def CloseApplication(event):  #event is passed on to our function
    r.destroy() # destroys the root window of tkinter application
    
def Submit_Rating():
        # creates a message widget in the sliderFrame with green background and width 200
        RatingMessage = tk.Message(SliderFrame,text="Thank you!\nHope to see you back!!",
                                   width=200,
                                   bg="green")
        RatingMessage.place(x=150,y=150)
    
   
    


def text_review():
    # gets the full string input from the text area
    input = text_area.get("1.0", "end-1c")
    # opens a file in write mode and writes what was inputted in the text area to that file
    review_file = open("Customer_Review.txt",'w')
    review_file.write(input)
    review_file.close() # closes the file
    
    #opens the file again this time in  read mode
    review_file=open("Customer_Review.txt","r")
    #prints what was written in the text area in the console window
    print(review_file.read())
    
    # display label with parent window -> SliderFrame, displays text with Arial font, size 10
    Review_message = tk.Label(SliderFrame,text="Thank you so much for the review!\nHave a great day!\nPress ESC to exit application",
                              font=("Arial",10))
    Review_message.place(x=110,y=530)
    
                            
#create tkinter window 
r = tk.Tk()

#make tkinter window not resizable
r.resizable(False,False)

#assign a title to tkinter window
r.title("Centra Greenpark")

#create a variable with a centra png
CentraBg = tk.PhotoImage(file="CentraBG.png")
#decrease size of the image
CentraBg = CentraBg.subsample(2,2)
#created canvas that will be displayed after login is successful
LoginCanvas = tk.Canvas(r,height=668,width=1085)  # 1100x675

#initizialise string variables
#will be used for the login section
readUsername = ""
usernameWord = ""
readPassword = ""
passwordWord = ""

#String variable with centra title message
CentraTitle = "Centra is Ireland's leading convenience retail group,\nwith 480 bright accessible stores in communities throughout the country"
#Centra mission string text containing centra mission
CentraMission = "We have a reputation for quality, value and friendly service\nand the fact that stores are independently owned\nand operated by local people means that shoppers \nget the best of both worlds:\n-Commitment to the traditional values of good fresh foods\n-Good fresh foods and excellent service\n\nCentra Stores provide you with convenient shopping\nsolutions, have all the items you need and are good\nvalue for money\n\nHappy to continue shopping?\n -Go to *Shopping* section\n\nWant to contact us?\n -Go to *Contact* section (please leave a review if u can!)"


# assigned all photoImages to variables that will be used to display items in the Shopping section as RadioButtons
# subsample was used to decrease height and width of the images so they relatively are all the same size
AppleImage = tk.PhotoImage(file="Apple.gif")
AppleImage = AppleImage.subsample(2,3)
SweetsImage = tk.PhotoImage(file="Sweets.gif")
SweetsImage = SweetsImage.subsample(5,5)
DonutImage = tk.PhotoImage(file="Donut.gif")
DonutImage = DonutImage.subsample(4,4)
CoffeeImage = tk.PhotoImage(file="Coffee.gif")
CoffeeImage = CoffeeImage.subsample(6,6)
CroissantImage = tk.PhotoImage(file="Croissant.gif")
CroissantImage = CroissantImage.subsample(3,4)
CremEggImage = tk.PhotoImage(file="CremEgg.gif")
CremEggImage = CremEggImage.subsample(7,7)
SlusheeImage = tk.PhotoImage(file="Slushee.gif")
SlusheeImage = SlusheeImage.subsample(2,3)
TeaImage = tk.PhotoImage(file="Tea.gif")
TeaImage = TeaImage.subsample(3,6)
BreadImage = tk.PhotoImage(file="Bread.gif")
BreadImage = BreadImage.subsample(10,10)
CakeImage = tk.PhotoImage(file="Cake.gif")
CakeImage = CakeImage.subsample(3,2)
AeroImage = tk.PhotoImage(file="Aero.gif")
AeroImage = AeroImage.subsample(2,2)
HunkyDoryImage = tk.PhotoImage(file="HunkyDory.gif")
HunkyDoryImage = HunkyDoryImage.subsample(2,3)
TaytoImage = tk.PhotoImage(file="Tayto.gif")
TaytoImage = TaytoImage.subsample(2,3)
StampImage = tk.PhotoImage(file="Stamp.gif")
StampImage = StampImage.subsample(10,10)
ChickenImage = tk.PhotoImage(file="Chicken.gif")
ChickenImage = ChickenImage.subsample(2,3)
CheeseImage = tk.PhotoImage(file="Cheese.gif")
CheeseImage = CheeseImage.subsample(5,5)
DogFoodImage = tk.PhotoImage(file="DogFood.gif")
DogFoodImage = DogFoodImage.subsample(15,17)
NutsImage = tk.PhotoImage(file="Nuts.gif")
NutsImage = NutsImage.subsample(4,5)
PenImage = tk.PhotoImage(file="Pen.gif")
PenImage = PenImage.subsample(6,7)
MuffinImage = tk.PhotoImage(file="Mufin.gif")
MuffinImage = MuffinImage.subsample(4,4)




#4 arrays that contain a counter, PhotoImage, name of Item and its price
# used to display the radiobuttons as items in the shopping section
#in order to display them in separate columns had to divide them into 4 different arrays

Items_left =  [(1,  AppleImage,         "Apple",        0.7),
              (2,  SweetsImage,         "Sweets",       1.2),
              (3,  DonutImage,          "Donut",        1.1),
              (4,  CoffeeImage,         "Coffee",       2.8),
              (5,  CroissantImage,      "Croissant",    0.8)]

          
         
Items_left01 =  [(1,  CremEggImage,     "CremEgg",     0.9),
                (2,  SlusheeImage,      "Slushee",     2.5),
                (3,  TeaImage,          "Tea",         2.3),
                (4,  BreadImage,        "Bread",         2),
                (5,  CakeImage,         "Cake",        5.5)]


Items_right =  [(1,  AeroImage,       "Aero",        1.4),
                (2,  HunkyDoryImage,  "HunkyDory",   2.7),
                (3,  TaytoImage,      "Tayto",       1.8),
                (4,  StampImage,      "Stamp",       1),
                (5,  ChickenImage,    "Chicken",     5.2)]

Items_right01 =  [(1,  CheeseImage,   "Cheese",      1.6),
                 (2,  DogFoodImage,  "DogFood",      6.5),
                 (3,  NutsImage,      "Nuts",        0.54),
                 (4,  PenImage,      "Pens",         0.35),
                 (5,  MuffinImage,   "Muffin",       1.5)]



#initialize variables
x1 = 0
y1 = 0

#initialize array that will store the names of Items selected in the Shopping section
nameArray = []
# variable used to get the price of items in the Shopping section
v = tk.DoubleVar()

#initialized variable, will be used to get sum of all prices of items selected in Shopping section
Sum_of_Prices = 0
#array that will store all the prices of items selected
AllPrices = []

#centra logo
CentraImage = tk.PhotoImage(file="Centra.gif")

# login gui label with Centra image on top
Centra = tk.Label(r,image=CentraImage,
                  width=390)
# display in row 0 column 1 in the grid
Centra.grid(row=0,column=1)


#text label telling the user to log their details below
#width 35 and pady 10 with custom background
Label01 = tk.Label(r,
                   text="Please enter details below to login",
                   width=35,
                   pady=10,
                   background="#C6F745")
Label01.grid(row=1,column=1,sticky=tk.N)


#Username text Label, padding is 10 pixels
UsernameLabel = tk.Label(r,text="Username*",
                   font="arial",
                   pady=10)
UsernameLabel.grid(row=2,column=1)


#variable that is used to get the string entered in the entry box for username login
Username = tk.StringVar()
#Entry box to input the username string, light blue background, relief is solid so the entry box looks as name says " solid "
UsernameEntry = tk.Entry(r,textvariable=Username,
                         bg="light blue",
                         relief="solid")
UsernameEntry.grid(row=3,column=1)






#Password text label , pady is extra space that is added above or below the text within the widget and assigned to 10
PasswordLabel = tk.Label(r,text="Password*",
                    font="arial",
                    pady=10)
#display to respective row and column in the grid
PasswordLabel.grid(row=4,column=1)

#String variable used to get the string entered in the password entry box
Password=tk.StringVar()
#Password entry box, instead of plain characters it puts "*" for security reasons using show option
#light blue background and solid relief making it look more solid
PasswordEntry = tk.Entry(r,textvariable=Password,
                         bg="light blue",
                         show="*",
                         relief="solid")
PasswordEntry.grid(row=5,column=1)


#useless label just to occupy space in order to display the login button further down
UselessLabel=tk.Label(r)
UselessLabel.grid(row=6)
#Login Button with command Centra_Login when pressed, blue background and yellow text foreground, when pressed executes command
LoginButton = tk.Button(r,text="Login",
                        bg="blue",
                        fg="yellow",
                        command=Centra_Login)
#displays at respective row column in the grid sticking up NORTH
LoginButton.grid(row=7,column=1,sticky=tk.N)

#another useless label to occupy space to display CreateNewAccount button further down
UselessLabel01 = tk.Label(r)
UselessLabel01.grid(row=8)

#Button that when pressed has command NewAccount_Display, where a new account can be created
#silver background and executes command when pressed
CreateNewAccount = tk.Button(r,text="Create a new Account?",
                             bg = "silver",
                             command = NewAccount_Display)
#displays at respective row column in the grid sticking up NORTH
CreateNewAccount.grid(row=9,column=1,sticky=tk.N)

#initialized button in main code, so it's easier to use later and call in between functions
CA = tk.Button(r)

# open 2 text files and read them, username and password
R01 = open("Username.txt")
Read_Username = R01.read()
R02 = open("Password.txt")
Read_Password = R02.read()

#Created a frame for the radiobutton items in the shopping section
TopSellersFrame = tk.Frame(r,width=1200,height=650)
#Right side frame in the shopping section
RSFrame = tk.Frame(r)

#Message widget initialized in main code for easier calls in between functions with main window RSFrame
M2 = tk.Message(RSFrame)

#Message widget with main window RSFrame in Shopping section, used later to display total items selected and their price
totalMessage = tk.Message(RSFrame)

#Label widget with main window RSFrame, yellow background, 250 width and size 10 with font type Open Sans
Search_label = tk.Message(RSFrame,text="Check if an item is in stock: ",
                          bg="yellow",width=250,font =('Open Sans',10))
# variable to get the string when searching an item in the Search_item entry box, after the search_button is pressed
Search = tk.StringVar()
#Search entry box with main window RSFrame and textvariable Search, width 30 and silver background,
#similar relief to previous entries
#initialized in the main code so easier to use in between functions
Search_item = tk.Entry(RSFrame,textvariable=Search,width=30,
                       relief="solid",
                       bg = "silver")

#Search button with main window RSFrame, green background
#executes command if pressed
Search_button = tk.Button(RSFrame,text="SEARCH ITEM",
                          bg = "green",
                          command=SearchItem)

#Button with parent window RSFrame and command AddtoBasket if pressed
Add_to_Basket = tk.Button(RSFrame,text="Add item to Basket",
                          command=AddtoBasket)

# Button with parent window RSFRame and command TotalPrice, custom background
total_price_topSellers = tk.Button(RSFrame,text="Calculate Total price",
                                   bg="#641994",
                                   command=TotalPrice)

# initialized vaiables that will be used to run through Items_on_Stock array
productName = ""
productPrice = 0

#Message widget with parent window RSframe, and 350 width
m1 = tk.Message(RSFrame,width=350)

# initialized variable
tempPrice = 0

# array with all the item names on stock and their prices
Items_on_stock =  [("Apple",       0.7),
                  ("Sweets",       1.2),
                  ("Donut",        1.1),
                  ("Coffee",       2.8),
                  ("Croissant",    0.8),
                  ("CremEgg",      0.9),
                  ("Slushee",      2.5),
                  ("Tea",          2.3),
                  ("Bread",          2),
                  ("Cake",         5.5),
                  ("Aero",         1.4),
                  ("HunkyDory",    2.7),
                  ("Tayto",        1.8),
                  ("Stamp",          1),
                  ("Chicken",      5.2),
                  ("Cheese",       1.6),
                  ("DogFood",      6.5),
                  ("Nuts",        0.54),
                  ("Pens",        0.35),
                  ("Muffin",       1.5)]


# finish shopping button with parent window RSFrame and command Finish, brown background
Finish = tk.Button(RSFrame,text="Finish Shopping",
                   bg = "brown",
                  command=Finish)

#Slider frame intialized in main code with parent window root tkinter
#will be used after finishing shopping button has been pressed
SliderFrame = tk.Frame(r)
# slider scale with values from 0 to 100 and displays horizontally, parent window is SliderFrame
Slider = tk.Scale(SliderFrame,from_=0,to=100, orient="horizontal")

#created a text area to be used as a way for the user to write feedback, parent window is SliderFrame
text_area = tk.Text(SliderFrame)

# Button for the text area, when pressed executes command text_review, parent window is SliderFrame
textArea_Button = tk.Button(SliderFrame,text="Submit Review",
                            command= text_review)


#created a frame with parent window root, will be used in the contact section
ContactFrame = tk.Frame(r)
# label widget with parent window ContactFrame
SelectLabel = tk.Label(ContactFrame)

# two variables that will be used to get the value of two checkbuttons in the contact section
t = tk.IntVar()
s = tk.IntVar()

# checkbuttons and labels  with parent windows ContactFrame
# will be used later to display info of the centra staff in the contact section
Manager = tk.Checkbutton(ContactFrame)
manager_info = tk.Label(ContactFrame)
Supervisor = tk.Checkbutton(ContactFrame)
supervisor_info = tk.Label(ContactFrame)


# infinite loop of tkinter window
r.mainloop()

        
    
    
   
        
   
    
    











                   

                       







