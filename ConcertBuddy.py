# imports necessary libraries
import tkinter as tk
from PIL import Image, ImageTk


# Code to create the gui window
root = tk.Tk()

# Code to configure the size
root.geometry("450x600")

# Create the frame for the first window
f1 = tk.Frame(root)
# Read the image you want to use for the first frame
img = Image.open('media/background.jpg')
# Resize the image
img = img.resize((450, 600), Image.LANCZOS)
# Add this code to view the image as the frame
pic = ImageTk.PhotoImage(img)
Lab = tk.Label(f1, image=pic)
Lab.pack()
f1.pack()

# The first page:

# Label to greet user
hello = tk.Label(root, text="Welcome to ConcertBuddy",
                 font="Segoeui 20",
                 bg="#F7D9FD",
                 fg="#7E32DB")
hello.place(x=60, y=20)

# Label to ask for the users name
name = tk.Label(root, text="Please enter your name to sign up:",
                font="SegoeUI 13 bold",
                fg="#7E32DB")
name.place(x=90, y=80)

# Create a box where the user can enter their name and save the input
input_name = tk.StringVar()
name_box = tk.Entry(root, textvariable=input_name,
                    font="SegoeUI 13",
                    fg="#7E32DB")
name_box.place(x=120, y=130)

# Label to ask for age
age = tk.Label(root, text="Please enter your age:",
               font="SegoeUI 13 bold",
               fg="#7E32DB")
age.place(x=90, y=180)

input_age = tk.StringVar()
age_box = tk.Entry(root, textvariable=input_age,
                   font="SegoeUI 13",
                   fg="#7E32DB")
age_box.place(x=120, y=220)

# Label to ask for gender
gender = tk.Label(root, text="Please enter your gender (f/m/d):",
                  font="SegoeUI 13 bold",
                  fg="#7E32DB")
gender.place(x=90, y=270)

input_gender = tk.StringVar()
gender_box = tk.Entry(root, textvariable=input_gender,
                      font="SegoeUI 13",
                      fg="#7E32DB")
gender_box.place(x=120, y=310)


# Definition for the second page:
def secondpage():
    # Destroys everything except the background of the first page
    hello.destroy()
    name.destroy()
    name_box.destroy()
    age.destroy()
    age_box.destroy()
    gender.destroy()
    gender_box.destroy()
    letsfindabuddy.destroy()


    # Makes the variables of this function accessible for all functions
    global hi_user, ready, yes_button, ticket_sale, profilepage

    # Labels and buttons of the second page:

    hi_user = tk.Label(text=f'Hi {input_name.get().upper()}',
                      font="SegoeUI 20 bold",
                       fg="#7E32DB",
                       bg="white")
    hi_user.place(x=60, y=20)

    ready = tk.Label(text="Ready to find a perfect concert buddy?",
                     font="SegoeUI 15",
                     fg = "#7E32DB",
                     bg = "white")
    ready.place(x=60, y=100)

    yes_button = tk.Button(text="YES!",
                           font="SegoeUI 18 bold",
                           bg="#7E32DB",
                           fg="white",
                           command=thirdpage)
    yes_button.place(x=160, y=150)

    # Button that leads to the ticket sale page
    ticket_sale = tk.Button(text="I have a ticket to sell!",
                            font="SegoeUI 13",
                            bg="#F7D9FD",
                            fg="#F12FD6",
                            command=ticketpage)
    ticket_sale.place(x=30, y=500)

    # Button that leads to the profile page of the user
    profilepage = tk.Button(text="my profile",
                            font="SegoeUI 13",
                            bg="#F7D9FD",
                            fg="#F12FD6",
                            command=profilepagepage)
    profilepage.place(x=320, y=500)


# Definition for the third page:
def thirdpage():
    # Destroys everything from the second page (except the background)
    hi_user.destroy()
    ready.destroy()
    yes_button.destroy()
    ticket_sale.destroy()
    profilepage.destroy()

    global concert, artist, artist_box, location, location_box, date, date_box, \
        interests, interests_dropdown, seating, dropdown, star, searchbuddy

    # Labels and buttons of the third page:

    concert = tk.Label(text="I need a buddy for this concert:",
                       font="SegoeUI 15 bold",
                       fg="#7E32DB",
                       bg="white")
    concert.place(x=60, y=20)

    # Label to ask artist name
    artist = tk.Label(text="Please enter the name of the artist*",
                      font="SegoeUI 12")
    artist.place(x=80, y=60)

    # Box for artist input
    input_artist = tk.StringVar()
    artist_box = tk.Entry(textvariable=input_artist,
                          font="SegoeUI 12",
                          bg="#F7D9FD")
    artist_box.place(x=80, y=90)

    # Label to ask location name
    location = tk.Label(text="Please enter the name of the location of the concert*",
                        font="SegoeUI 12")
    location.place(x=80, y=130)

    # Box for location input
    input_location = tk.StringVar()
    location_box = tk.Entry(textvariable=input_location,
                            font="SegoeUI 12",
                            bg="#F7D9FD")
    location_box.place(x=80, y=160)

    # Label to ask for the date
    date = tk.Label(text="Please enter the date of the concert*",
                    font="SegoeUI 12")
    date.place(x=80, y=200)

    # Box for the date input
    input_date = tk.StringVar()
    date_box = tk.Entry(textvariable=input_date,
                        font="SegoeUI 12",
                        bg="#F7D9FD")
    date_box.place(x=80, y=230)

    # Label to ask for interests
    interests = tk.Label(text="Please choose three interests",
                         font="SegoeUI 12")
    interests.place(x=80, y=270)

    # Placeholder for drop-down menu for interests
    interests_dropdown = tk.Label(text="Here would be a drop-down menu to choose",
                                  font="SegoeUI 12",
                                  bg="#F7D9FD")
    interests_dropdown.place(x=80, y=300)

    # Label to ask about seating
    seating = tk.Label(text="You can also enter your seat or standing category",
                       font="SegoeUI 12")
    seating.place(x=80, y=340)

    dropdown = tk.Label(text="""Here would be a drop-down menu
     to select the seat/standing category""",
                        font="SegoeUI 12",
                        bg="#F7D9FD")
    dropdown.place(x=80, y=370)

    star = tk.Label(text="*the starred categories are necessary to fill out.",
                    font="SegoeUI 8",
                    bg="#F7D9FD")
    star.place(x=30, y=570)

    # Button to start the search of a buddy
    searchbuddy = tk.Button(text="search a buddy!",
                            font="SegoeUI 14 bold",
                            bg="#7E32DB",
                            fg="white",
                            command=searchpage)
    searchbuddy.place(x=120, y=420)



def searchpage():
    # Destroys everything from the third page (except background)
    concert.destroy()
    age.destroy()
    age_box.destroy()
    gender.destroy()
    gender_box.destroy()
    artist.destroy()
    artist_box.destroy()
    location.destroy()
    location_box.destroy()
    date.destroy()
    date_box.destroy()
    interests.destroy()
    interests_dropdown.destroy()
    seating.destroy()
    dropdown.destroy()
    star.destroy()
    searchbuddy.destroy()

    global searchresults, filter_button

    searchresults = tk.Label(text="""here would be the profiles of other users 
    that go to the selected concert 
    and the user could swipe left or right to connect with them""",
    fg = "#7E32DB",
    bg = "#F7D9FD")
    searchresults.place(x=50, y=130)

    # filter button
    filter_button = tk.Button(text="filter",
                              font="SegoeUI 10 bold",
                              bg="#F7D9FD",
                              fg="#7E32DB",
                              command=filterpage)
    filter_button.place(x=360, y=20)

def filterpage():
    # Destroys searchpage
    searchresults.destroy()
    filter_button.destroy()

    global filter_label, back_to_search

    filter_label = tk.Label(text="""the user could filter age, gender and interests
    of other users here""",
    font="SegoeUI 12",
    fg="#7E32DB",
    bg="#F7D9FD",)
    filter_label.place(x=40, y=150)

    # Button to go back to search
    back_to_search = tk.Button(text="BACK!",
                               font="SegoeUI 12 bold",
                               bg="#7E32DB",
                               fg="white",
                               command=backtosearch)
    back_to_search.place(x=40, y=400)

def backtosearch():
    filter_label.destroy()
    back_to_search.destroy()
    searchpage()

def ticketpage():

    hi_user.destroy()
    ready.destroy()
    yes_button.destroy()
    ticket_sale.destroy()
    profilepage.destroy()

    global ticketsale, goback

    ticketsale = tk.Label(text="this page is still under construction",
                          fg = "#7E32DB",
                          bg = "#F7D9FD")
    ticketsale.place(x=60, y=130)

    # Button to go back to the second page
    goback = tk.Button(text="BACK!",
                       command=backbutton,
                       fg = "white",
                       bg = "#7E32DB")
    goback.place(x=60, y=200)


# Definition for the button to go back to the second page
def backbutton():

    ticketsale.destroy()
    goback.destroy()

    secondpage()


def profilepagepage():

    hi_user.destroy()
    ready.destroy()
    yes_button.destroy()
    ticket_sale.destroy()
    profilepage.destroy()

    global hi_user_2, spotify, goback2

    hi_user_2 = tk.Label(text=f'Hi {input_name.get().upper()}',
                         font="SegoeUI 20 bold",
                         fg="#7E32DB",
                         bg="white")
    hi_user_2.place(x=60, y=20)

    spotify = tk.Label (text="Here would be the spotify or apple music info of the user",
                        height=20,
                        width=50,
                        fg="#7E32DB",
                        bg="#F7D9FD")
    spotify.place (x=60, y=70)

    # Button to go back to the second page
    goback2= tk.Button(text="BACK!",
                       fg="white",
                       bg="#7E32DB",
                       command=backbutton2)
    goback2.place(x=60, y=400)


# Definition for the second button to go back to the second page
def backbutton2():

    hi_user_2.destroy()
    spotify.destroy()
    goback2.destroy()

    secondpage()


# Adds a button to start
letsfindabuddy = tk.Button(text="Lets find a buddy!",
                           font="SegoeUI 14 bold",
                           bg="#7E32DB",
                           fg="white",
                           command=secondpage)
letsfindabuddy.place(x=120, y=360)


# Press enter to trigger the find a buddy button
def enternextpage(event):
    secondpage()

# Code that will enter the game when you press enter
name_box.bind('<Return>',
              enternextpage)

# Code to execute the code
root.mainloop()

