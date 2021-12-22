from tkinter import *
import tkinter as tk
from winsound import *
import winsound
from tkinter import messagebox
root = Tk()  
root.geometry("1000x600") 
root.title("Create by VANSAO & SOPHA")
root.resizable(0,0)
canvas = Canvas( root, width = 800, height = 600) 
canvas.pack(fill = "both", expand = True) 
# Variable................................................................................................
clicksound = True

# Function ....................................................................................................................

# Display sound................................................................................................................
def displaysound():
    global clicksound
    if clicksound:
        winsound .PlaySound("Sounds.\click.wav", winsound.SND_FILENAME)
def remove(event):
    displaysound()
    canvas.delete("remove")
    canvas.delete("delete")
    canvas.delete("musicon")
    canvas.delete("aboutText")
    canvas.move("welcome", 0, 100)


# about game...............................................................................................................
def about(event):
    displaysound()
    canvas.move("welcome", 0, -100)
    canvas.create_rectangle(300, 150, 700, 400, fill="white", tags="delete")
    canvas.create_text(680, 165, text = "X", fill="red", font="Purisa", tags="remove")
    canvas.create_text(330, 190, anchor=W, font="Purisa",text="- Step1: Click start to choose levels.", tags="aboutText")
    canvas.create_text(330, 220, anchor=W, font="Purisa",text="- Step2: Use arrow key for movement.", tags="aboutText")
    canvas.create_text(330, 250, anchor=W, font="Purisa",text="- Step3: Push the each box cover each diamond.", tags="aboutText")
    canvas.create_text(330, 280, anchor=W, font="Purisa",text="- If the all boxes cover all diamonds it will Win", tags="aboutText")
    canvas.create_text(330, 310, anchor=W, font="Purisa",text="- If you push the box more than 100 times", tags="aboutText")
    canvas.create_text(345, 340, anchor=W, font="Purisa",text="Game over!", tags="aboutText")
## Exit window
def exitgame(event):
    global root
    root.quit()
    winsound .PlaySound("Sounds.\click.wav", winsound.SND_FILENAME)
canvas.tag_bind("exit","<Button-1>", exitgame)
# #Start game.....................................................................................................................
def startbg():
    global bg
    canvas.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
    # Add Text 
    canvas.create_text(500, 150, text = "Welcome to the sukobane!!!", fill="#fff", font="Times 35 italic bold", tags="welcome")
    #Start
    canvas.create_rectangle(430, 220, 610, 280, fill="#784428", tags="start")
    canvas.create_text(515, 250, text = "START", fill="white", font="Times 35 italic bold", tags="start")

    # about
    canvas.create_rectangle(430, 320, 610, 380, fill="#784428", tags="quit")
    canvas.create_text(515, 350, text = "ABOUT", fill="white", font="Times 35 italic bold", tags="quit")
    
    # exit
    canvas.create_rectangle(430, 420, 610, 480, fill="#784428", tags="exit")
    canvas.create_text(515, 450, text = "EXIT", fill="white", font="Times 35 italic bold", tags="exit")
    
# First of game...............................................................................................................
def begin():
    canvas.create_text(500, 550, text = "Loading...", fill="white", font="Times 20 italic bold", tags="welcome")
    canvas.after(2000, startbg)

# ClickOn.....................................................................................................................
canvas.tag_bind("start", "<Button-1>")
canvas.tag_bind("quit", "<Button-1>", about)
canvas.tag_bind("remove", "<Button-1>", remove)
# Image........................................................................................................................
bg = PhotoImage(file ="images.\start.png") 
canvas.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
begin()
# Execute tkinter 
root.mainloop()
