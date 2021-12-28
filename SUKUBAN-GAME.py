from tkinter import *
import tkinter as tk
from typing import Counter
from winsound import *
import winsound
from tkinter import messagebox
root = tk.Tk()  
root.geometry("1000x600") 
root.resizable(0,0)
frame = tk.Frame()
canvas = tk.Canvas(frame)
canvas.pack(fill = "both", expand = True) 
frame.pack(fill = "both", expand = True) 
# Variable................................................................................................

diamondcondition = False
levels=1
grid = []
score = 0
boxcounter = 0
iswin = False
#imgages
img = tk.PhotoImage(file="images\mario.png")
diamond = tk.PhotoImage(file="images\diamond2.png")
diamond1 = tk.PhotoImage(file="images\diamond.png")
wall = tk.PhotoImage(file="images\wall.png")
box = tk.PhotoImage(file="images\imgbox.png")
background = tk.PhotoImage(file="images\imgbackground.png")
grass = tk.PhotoImage(file="images\grass.png")
detail = tk.PhotoImage(file="images\imgaboutgame.png")
startb = tk.PhotoImage(file="images\startb.png")
aboutb = tk.PhotoImage(file="images\imgaboutb.png")
exitb = tk.PhotoImage(file="images\exitb.png")
backbutton = tk.PhotoImage(file="images\imgbackb.png")
win = tk.PhotoImage(file="images\win.png")
next = tk.PhotoImage(file="images\imgnext.png")
restart = tk.PhotoImage(file="images\imgrestart.png")
# Function ....................................................................................................................

# Display sound................................................................................................................


#__________________________get grid from files_______________________________ 
def getgrid():
    global levels
    file = open("files\\"+"level"+str(levels)+".txt")
    grid = file.read()
    grid = grid.split('|')
    for i in range(len(grid)):
        grid[i] = grid[i].strip('\n')
        grid[i] = grid[i].split(',')
        for j in range(len(grid[i])):
            grid[i][j] = int(grid[i][j])
    file.close()
    return grid
grid = getgrid()
# _________________________drwagrid__________________________________
def drawgrid():
    global grid,score, boxcounter,levels,diamondcondition
    canvas.delete("all")
    getgrid()
    canvas.create_image(0,0,anchor="nw",image = background)
    scores=canvas.create_text(860,60,text="Scores: "+str(score), fill="brown", font=('Helvetica 25 bold'))
    canvas.create_text(850,100,text="Levels: "+str(levels), fill="brown", font=('Helvetica 25 bold'))
    boxcounter =  0
    canvas.create_image(50,40,anchor="nw",image = backbutton,tag="back")
    canvas.create_image(800,450,anchor="nw",image = restart,tag="restart")
    X1=0
    y1 = 80
    y2 = 140
    for row in range(len(grid)):
        x1 = 200
        x2 = 260
        for col in range(len(grid[0])):
            x1+=60
            x2+=60
            if grid[row][col] == 1:
                canvas.create_image(x2-30,y2-30,image=grass) 
                canvas.create_image(x2-30,y2-30,image=img)
            elif grid[row][col] == 2:
                canvas.create_image(x2-30,y2-30,image=grass) 
                canvas.create_image(x2-30,y2-30,image=diamond)
            elif grid[row][col] == 3:
                canvas.create_image(x2-30,y2-30,image=wall)
            elif grid[row][col] == 0:
                canvas.create_image(x2-30,y2-30,image=grass) 
            elif grid[row][col] == 5:
                canvas.create_image(x2-30,y2-30,image=box)
                boxcounter += 1
                X1+=40
                canvas.create_image(755+X1,150,image=diamond1)
        y1+=60
        y2+=60
  
    diamondIndex = getDiamondIndex()
    if diamondIndex==[] and levels<8:
        canvas.create_image(900,500,image= next,tags = "start")        
        levels +=1
        diamondcondition = False
        grid = getgrid()
        score += boxcounter*10
        canvas.delete(scores)
        canvas.delete("restart")
        scores=canvas.create_text(860,60,text="Scores: "+str(score), fill="brown", font=('Helvetica 25 bold'))
        canvas.create_image(500,300,image= win)
        

    print(boxcounter)
def displaysound():
        winsound .PlaySound("Sounds.\click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
def gamesound():
    winsound .PlaySound("Sounds.\music-game.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
def remove(event):
    displaysound()
    canvas.delete("remove")
    canvas.delete("delete")
    canvas.delete("aboutText")
    canvas.move("welcome", 0, 100)

def getindex1():
    global grid
    index1 = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                index1.append(i)
                index1.append(j)
    return index1
# get index of diamond
def getDiamondIndex():
    global grid
    diamondIndex = []
    for row in range(len(grid)):
        array= []
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                array.append(row)
                array.append(col)
                diamondIndex.append(array)
    return diamondIndex

# get index of the box
def getBoxIndex():
    global grid
    boxIndex = []
    for rowbox in range(len(grid)):
        
        for colbox in range(len(grid[0])):
            arraybox= []
            if grid[rowbox][colbox] == 5:
                arraybox.append(rowbox)
                arraybox.append(colbox)
                boxIndex.append(arraybox)
    return boxIndex


def moveRight(event):
    global grid,diamondcondition,diamondcolIndex,diamondrowIndex
    index = getindex1()
    rowIndex1 = index[0]
    colIndex1 = index[1]
    if grid[rowIndex1][colIndex1+1] != 3:
        
        if diamondcondition :
            if  grid[rowIndex1][colIndex1+1] != 2:
                diamondcondition = False
            if grid[rowIndex1][colIndex1+2] != 5:
                if grid[rowIndex1][colIndex1+1] == 5:
                    grid[rowIndex1][colIndex1+2]=5
            grid[rowIndex1][colIndex1]=0
            grid[rowIndex1][colIndex1]=2
            grid[rowIndex1][colIndex1+1]=1
        elif grid[rowIndex1][colIndex1+1] == 5 and grid[rowIndex1][colIndex1+2] != 3 and grid[rowIndex1][colIndex1+2] != 5:
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                    grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            if grid[rowIndex1][colIndex1+2] == 2:
                diamondrowIndex = rowIndex1
                diamondcolIndex = colIndex1+2
            grid[rowIndex1][colIndex1+1]=1
            grid[rowIndex1][colIndex1+2]=5

        elif grid[rowIndex1][colIndex1+1] != 5 and not diamondcondition:
            if grid[rowIndex1][colIndex1+1] == 2:
                diamondcondition = True
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            grid[rowIndex1][colIndex1+1]=1
        

    drawgrid()
    # win()
    
def moveLeft(event):
    global grid,diamondcondition,diamondrowIndex,diamondcolIndex
    index = getindex1()
    rowIndex1 = index[0]
    colIndex1 = index[1]
    if grid[rowIndex1][colIndex1-1] != 3:
        if diamondcondition :
            if grid[rowIndex1][colIndex1-1] != 2:
                diamondcondition = False
            if grid[rowIndex1][colIndex1-2] != 5:
                if grid[rowIndex1][colIndex1-1] == 5:
                    grid[rowIndex1][colIndex1-2]=5
            grid[rowIndex1][colIndex1]=0
            grid[rowIndex1][colIndex1]=2
            grid[rowIndex1][colIndex1-1]=1
        elif grid[rowIndex1][colIndex1-1] == 5 and grid[rowIndex1][colIndex1-2] != 3 and grid[rowIndex1][colIndex1-2] != 5:

            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                    grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            if grid[rowIndex1][colIndex1-2] == 2:
                diamondrowIndex = rowIndex1
                diamondcolIndex = colIndex1-2
            grid[rowIndex1][colIndex1-1]=1
            grid[rowIndex1][colIndex1-2]=5
        elif grid[rowIndex1][colIndex1-1] != 5  and  not diamondcondition:
            if grid[rowIndex1][colIndex1-1] == 2:
                diamondcondition = True
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            grid[rowIndex1][colIndex1-1]=1
    drawgrid()
    # win()
diamondrowIndex = 0
diamondcolIndex = 0
isdiamondindex = False
def moveDown(event):
    global grid,diamondcondition, diamondcolIndex,diamondrowIndex
    index = getindex1()
    rowIndex1 = index[0]
    colIndex1 = index[1]
    print(diamondcondition)
    if grid[rowIndex1+1][colIndex1] != 3:
        if diamondcondition :
            if grid[rowIndex1+1][colIndex1] != 2:
                diamondcondition = False
            if grid[rowIndex1+2][colIndex1] != 5:
                if grid[rowIndex1+1][colIndex1] == 5:
                    grid[rowIndex1+2][colIndex1]=5 
            grid[rowIndex1][colIndex1]=2
            grid[rowIndex1+1][colIndex1]=1
        elif grid[rowIndex1+1][colIndex1] == 5 and grid[rowIndex1+2][colIndex1] != 3 and grid[rowIndex1+2][colIndex1] != 5 :

            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                    grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            if grid[rowIndex1+2][colIndex1] == 2:
                diamondrowIndex = rowIndex1+2
                diamondcolIndex = colIndex1
            grid[rowIndex1+1][colIndex1]=1
            grid[rowIndex1+2][colIndex1]=5
        elif grid[rowIndex1+1][colIndex1] != 5 and not diamondcondition:
            if grid[rowIndex1+1][colIndex1] == 2:
                diamondcondition = True
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            grid[rowIndex1+1][colIndex1]=1
    drawgrid()
    # win()

def moveUp(event):
    global grid, diamondcondition,diamondcolIndex,diamondrowIndex
    index = getindex1()
    rowIndex1 = index[0]
    colIndex1 = index[1]
    if grid[rowIndex1-1][colIndex1] != 3:
        if grid[rowIndex1-1][colIndex1] != 5 and not diamondcondition :
            if grid[rowIndex1-1][colIndex1] == 2:
                diamondcondition = True
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            grid[rowIndex1-1][colIndex1]=1
        elif diamondcondition and grid[rowIndex1-2][colIndex1] != 3:
            if grid[rowIndex1-1][colIndex1] != 2:
                diamondcondition = False
            if grid[rowIndex1-2][colIndex1] != 5 and grid[rowIndex1-1][colIndex1] != 3:
                if grid[rowIndex1-1][colIndex1] == 5:
                    grid[rowIndex1-2][colIndex1]=5 
            grid[rowIndex1][colIndex1]=2
            grid[rowIndex1-1][colIndex1]=1
        elif grid[rowIndex1-1][colIndex1] == 5 and grid[rowIndex1-2][colIndex1] != 3 and grid[rowIndex1-2][colIndex1] != 5 :

            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                    grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            if grid[rowIndex1-2][colIndex1] == 2:
                diamondrowIndex = rowIndex1-2
                diamondcolIndex = colIndex1
            grid[rowIndex1-1][colIndex1]=1
            grid[rowIndex1-2][colIndex1]=5
        elif grid[rowIndex1-1][colIndex1] != 5 and not diamondcondition:
            if grid[rowIndex1-1][colIndex1] == 2:
                diamondcondition = True
            if rowIndex1== diamondrowIndex and colIndex1 == diamondcolIndex:
                grid[rowIndex1][colIndex1]=2
            else:
                grid[rowIndex1][colIndex1]=0
            grid[rowIndex1-1][colIndex1]=1
    drawgrid()
    # win()
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)
root.bind("<Down>",moveDown)
root.bind("<Up>",moveUp)
#start game
def start(event):
    displaysound()
    drawgrid()
# about game...............................................................................................................
def about(event):
    displaysound()
    canvas.move("welcome", 0, -100)
    canvas.create_image(510, 270,image=detail, tags="aboutText")
    canvas.create_text(680, 175, text = "X", fill="red", font=('Helvetica 24 bold'), tags="remove")
## Exit window
def exitgame(event):
    global root
    root.quit()
    winsound .PlaySound("Sounds.\click.wav", winsound.SND_FILENAME)
canvas.tag_bind("exit","<Button-1>", exitgame)
# #Start game.....................................................................................................................
def startbg():
    global bg
    gamesound()
    canvas.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
    # Add Text 
    canvas.create_text(500, 150, text = "Welcome to the sukobane!!!", fill="#22BBEA", font="Times 35 italic bold", tags="welcome")
    #Start
    canvas.create_image(515,250, image = startb, tags = "start")
    # about 
    canvas.create_image(515,350, image = aboutb, tags = "quit")
    # exit
    canvas.create_image(515,450, image = exitb, tags = "exit")
#restart
def restart_game(event):
    global grid
    grid = getgrid()
    canvas.after(200,drawgrid)
### back
def back(event):
    startbg()
    winsound .PlaySound("Sounds.\click.wav", winsound.SND_FILENAME)
canvas.tag_bind("back","<Button-1>", back)
# First of game...............................................................................................................
def begin():
    gamesound()
    canvas.create_text(500, 550, text = "Loading...", fill="white", font="Times 20 italic bold", tags="welcome")
    canvas.after(2000, startbg)

# ClickOn.....................................................................................................................
canvas.tag_bind("start", "<Button-1>",start)
canvas.tag_bind("restart", "<Button-1>",restart_game)
canvas.tag_bind("quit", "<Button-1>", about)
canvas.tag_bind("remove", "<Button-1>", remove)
# Image........................................................................................................................
bg = PhotoImage(file ="images.\start.png") 
canvas.create_image( 0, 0, image = bg, anchor = "nw", tags="bg1")
begin()
# Execute tkinter 
root.mainloop()
