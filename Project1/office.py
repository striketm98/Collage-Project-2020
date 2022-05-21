from tkinter import*

def main_screen():

# The first screen configuration#####################
    global screen
    
################# screen diagram ####################
    screen = Tk()
    screen.geometry("1280x1200")
    screen.title("office-1.0")
    screen["background"]='#F88158'

#################### screen heading function #######################
    Label(text="ABC Office System",bg="#F88158",height="4",width="500",font=("Times",30,"bold")).pack() 
###################### Registration section ###########################

    global Name 
    global employee_id
    global dob
    global contact_no
    global address

    Name=StringVar()
    employee_id=StringVar()
    dob=StringVar()
    contact_no=StringVar()
    address=StringVar()

############################### Registration Labeling##############################

    Label(screen,).pack()

    screen.mainloop()
main_screen()    