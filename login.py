from tkinter import *
from PIL import Image, ImageTk  # For jpg image support

def main_screen():
    screen = Tk()
    screen.title("Login App")
    screen.geometry("400x500")
    screen.config(bg="white")

    # Load and display JPG image using Pillow
    try:
        img = Image.open("login.jpg")
        img = img.resize((400, 200))  # Resize image to fit nicely
        image_icon = ImageTk.PhotoImage(img)
        label = Label(screen, image=image_icon, bg="white")
        label.image = image_icon  # Keep a reference
        label.pack(pady=10)
    except Exception as e:
        print("Image error:", e)

    # Login label
    Label(screen, text="Login", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    # Username and password fields
    Label(screen, text="Username:", font=("Arial", 12), bg="white").pack()
    username_entry = Entry(screen, font=("Arial", 12))
    username_entry.pack(pady=5)

    Label(screen, text="Password:", font=("Arial", 12), bg="white").pack()
    password_entry = Entry(screen, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # Login button
    def login():
        username = username_entry.get()
        password = password_entry.get()
        print("Username:", username)
        print("Password:", password)

    Button(screen, text="Login", command=login, bg="#4CAF50", fg="white", font=("Arial", 12), width=20).pack(pady=15)

    screen.mainloop()

main_screen()
