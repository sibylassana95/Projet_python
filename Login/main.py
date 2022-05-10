from tkinter import *


# Creation des variable
def login():
    # getting form data
    nom = username.get()
    mot_de_pass = password.get()
    # validation du formulaire
    if nom == '' or mot_de_pass == '':
        message.set("Veuillez saisir vos information!")
    else:
        if nom == "siby" and mot_de_pass == "abc":
            message.set("Connexion reusi !")
        else:
            message.set("nom ou mot de passe incorrect!!!")


# defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    login_screen.geometry("300x250")
    # declaring variable
    global message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Connexion", bg="orange", fg="white").pack()
    # Username Label
    Label(login_screen, text="Username * ").place(x=20, y=40)
    # Username textbox
    Entry(login_screen, textvariable=username).place(x=90, y=42)
    # Password Label
    Label(login_screen, text="Password * ").place(x=20, y=80)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=95, y=100)
    # Login button
    Button(login_screen, text="Se connecter", width=10, height=1, bg="orange", command=login).place(x=105, y=130)
    login_screen.mainloop()


# calling function Loginform
Loginform()
