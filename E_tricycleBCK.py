from tkinter import*
import os

def Login():
    global=screen2
    screen2=Toplevel(screen)
    screen2.title("E-tricycle Commercial ")
def main_screen(): 
    global screen
    screen = Tk()
    screen.geometry("600x400")
    screen.title("E-tricycle Commercial")
    Label(text="E-tricycle Commercial",bg="white",width="300",height="2",font=("Calebri",20,"bold")).pack()
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command="Login").pack()
    screen.mainloop()
main_screen()    

