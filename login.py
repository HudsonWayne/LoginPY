from tkinter import *
from tkinter import messagebox
import os 


def main_screen():
    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")
    
    
    image_icon = PhotoImage(file= "icon.png")
    screen.iconphoto(False,image_icon)
    
    screen.title("Login System")
    
    lblTitle=Label(text = "Login System",font = ("Arial",50,'bold'),fg="black", bg="#d7dae2")
    
main_screen()