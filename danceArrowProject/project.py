
"""
Dance Arrow Game:
As arrows scroll downwards on the screen, when they meet a stationary set of target arrows, presses the corresponding
arrows (left arrow, down arrow, up arrow or right arrow) on the keyboard.
"""

# library
import Tkinter as Tk
import random as rd
import math
from PIL import ImageTk
import random
import time
import pygame
import os

# global variables
WIDTH = 1500.0
HEIGHT = 750.0
SPEED = 30

##########################################Start of arrow####################################################
### moving arrow
class arrow(object):
    ## arrows setup
    def __init__(self, canvas):
        self.canvas = canvas
        
        # blue arrows
        self.left = ImageTk.PhotoImage(file = "bleft.png")
        self.down = ImageTk.PhotoImage(file = "bdown.png")
        self.up = ImageTk.PhotoImage(file = "bup.png")
        self.right = ImageTk.PhotoImage(file = "bright.png")
        
        # red arrows
        self.rleft = ImageTk.PhotoImage(file = "rleft.png")
        self.rdown = ImageTk.PhotoImage(file = "rdown.png")
        self.rup = ImageTk.PhotoImage(file = "rup.png")
        self.rright = ImageTk.PhotoImage(file = "rright.png")

        # the y position (height) of the arrows at the beginning
        self.y = 10
        self.ry = 10
        
        # randomly pick a direction of arrows (left, down, up, right) and colors (blue or red)
        number = random.randint(1, 8)
        if (number == 1):
            self.symbol = "left"
            self.x = WIDTH/7
            self.image = self.canvas.create_image(self.x, self.y, image = self.left, anchor = "nw")
        elif (number == 2):
            self.symbol = "down"
            self.x = WIDTH/7*2
            self.image = self.canvas.create_image(self.x, self.y, image = self.down, anchor = "nw")
        elif (number == 3):
            self.symbol = "up"
            self.x = WIDTH/7*3
            self.image = self.canvas.create_image(self.x, self.y, image = self.up, anchor = "nw")
        elif (number == 4):
            self.symbol = "right"
            self.x = WIDTH/7*4
            self.image = self.canvas.create_image(self.x, self.y, image = self.right, anchor = "nw")
        elif (number == 5):
            self.symbol = "rleft"
            self.rx = WIDTH/7
            self.rimage = self.canvas.create_image(self.rx, self.ry, image = self.rleft, anchor = "nw")
        elif (number == 6):
            self.symbol = "rdown"
            self.rx = WIDTH/7*2
            self.rimage = self.canvas.create_image(self.rx, self.ry, image = self.rdown, anchor = "nw")
        elif (number == 7):
            self.symbol = "rup"
            self.rx = WIDTH/7*3
            self.rimage = self.canvas.create_image(self.rx, self.ry, image = self.rup, anchor = "nw")
        elif (number == 8):
            self.symbol = "rright"
            self.rx = WIDTH/7*4
            self.rimage = self.canvas.create_image(self.rx, self.ry, image = self.rright, anchor = "nw")


    ## update the position of arrows
    def arrow_update(self):
        if (self.symbol == "left" or self.symbol == "down" or self.symbol == "up" or self.symbol == "right"):
            self.canvas.move(self.image, 0, 10)
            self.y += 10
        else:
            self.canvas.move(self.rimage, 0, 10)
            self.ry += 10

    ## return the position of blue arrows
    def position(self):
        if (self.symbol == "rleft" or self.symbol == "rdown" or self.symbol == "rup" or self.symbol == "rright"):
            return (0,0)
        x = self.canvas.coords(self.image)
        return x

    ## return the position of red arrows
    def rposition(self):
        if (self.symbol == "left" or self.symbol == "down" or self.symbol == "up" or self.symbol == "right"):
            return (0,0)
        x = self.canvas.coords(self.rimage)
        return x

##########################################End of arrow####################################################

##########################################Start of arrowGame##############################################
# game
class arrowGame(object):
    ## game setup
    def __init__(self, master):
        self.master = master
        
        self.canvas = Tk.Canvas(width = WIDTH, height = HEIGHT, bg = 'white')
        self.canvas.pack(expand = "YES", fill = "both")
        self.image = ImageTk.PhotoImage(file = "background.jpg")
        self.canvas.create_image(10, 10, image = self.image, anchor = "nw")
        
        self.startButton = Tk.Button(master, text="Start", command = self.start)
        self.startButton.pack()
        self.startButton.place(x=WIDTH/4*3, y=HEIGHT/4)
        
        self.quitButton = Tk.Button(master, text="Quit", command = self.quit)
        self.quitButton.pack()
        self.quitButton.place(x=WIDTH/4*3, y=HEIGHT/4+50)
        
        self.level = 1
        self.levelLabel = Tk.Label(master, text="level %d/25" % self.level)
        self.levelLabel.pack()
        self.levelLabel.place(x=WIDTH/4*3, y=HEIGHT/4+100)
        
        self.score = 0
        self.scoreLabel = Tk.Label(master, text="%d points!" % self.score)
        self.scoreLabel.pack()
        self.scoreLabel.place(x=WIDTH/4*3, y=HEIGHT/4+150)
        
        self.scoreImage = ImageTk.PhotoImage(file = "score.png")
        self.canvas.create_image(WIDTH/4*3+190, HEIGHT/4+30, image = self.scoreImage , anchor = "nw")
        
        
        self.canvas.create_text(WIDTH/4*3.2+60,HEIGHT/4*3.3-80,fill="light blue",font="Times 15 bold",
                                text="                              Rule: \n Button: LEFT, DOWN, UP, RIGHT arrow. \n As arrows scroll downwards on the screen, \n when they meet stationary target arrows, \n presses the corresponding arrows. \n You will earn 1 point for blue arrow. \n You will lose 5 points for red arrow. \n You will win when you finished 25 levels. \n You will need to earn 5 points to level up. \n You will lose if you have negative score. \n Press the quit button to end your game. \n Press the start button to begin. Enjoy!")
            
        self.left = ImageTk.PhotoImage(file = "left.png")
        self.canvas.create_image(WIDTH/7, HEIGHT/4*3.5, image=self.left, anchor='nw')
        
        self.down = ImageTk.PhotoImage(file = "down.png")
        self.canvas.create_image(WIDTH/7*2, HEIGHT/4*3.5, image=self.down, anchor='nw')
        
        self.up = ImageTk.PhotoImage(file = "up.png")
        self.canvas.create_image(WIDTH/7*3, HEIGHT/4*3.5, image=self.up, anchor='nw')
        
        self.right = ImageTk.PhotoImage(file = "right.png")
        self.canvas.create_image(WIDTH/7*4, HEIGHT/4*3.5, image=self.right, anchor='nw')
        
        self.dleft = ImageTk.PhotoImage(file = "dleft.png")
        self.dfigure = self.canvas.create_image(WIDTH/4*3+100, HEIGHT/4, image=self.dleft, anchor='nw')
        
        self.alive = True
        self.arrow_group = []
        self.move()

    ## start music and get the moving arrows
    def start(self):
        # loop music
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(os.path.join(os.getcwd(), 'music.wav'))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
        
        self.startButton['state'] = Tk.DISABLED
        
        a_arrow = arrow(self.canvas)
        self.arrow_group.append(a_arrow)
        self.canvas.after(500, self.addArrow)
    
    ## add new arrows
    def addArrow(self):
        a_arrow = arrow(self.canvas)
        self.arrow_group.append(a_arrow)
        if self.alive:
            times = self.level*10
            self.canvas.after(400 - times, self.addArrow)

    ## update level and score
    def update_label(self):
        self.scoreLabel["text"] = "%d points" % self.score
        self.levelLabel["text"] = "level %d/25" % self.level

    ## flash the arrows if the arrow buttons are clicked on correct timing
    def flash(self, direction):
        if (direction == "left"):
            self.left = ImageTk.PhotoImage(file = "leftb.png")
            self.canvas.create_image(WIDTH/7, HEIGHT/4*3.5, image=self.left, anchor='nw')
        elif (direction == "down"):
            self.down = ImageTk.PhotoImage(file = "downb.png")
            self.canvas.create_image(WIDTH/7*2, HEIGHT/4*3.5, image=self.down, anchor='nw')
        elif (direction == "up"):
            self.up = ImageTk.PhotoImage(file = "upb.png")
            self.canvas.create_image(WIDTH/7*3, HEIGHT/4*3.5, image=self.up, anchor='nw')
        elif (direction == "right"):
            self.right = ImageTk.PhotoImage(file = "rightb.png")
            self.canvas.create_image(WIDTH/7*4, HEIGHT/4*3.5, image=self.right, anchor='nw')

    ## retore the flashed arrows to its original state
    def restore(self, direction):
        if (direction == "left"):
            self.left = ImageTk.PhotoImage(file = "left.png")
            self.canvas.create_image(WIDTH/7, HEIGHT/4*3.5, image=self.left, anchor='nw')
        elif (direction == "down"):
            self.down = ImageTk.PhotoImage(file = "down.png")
            self.canvas.create_image(WIDTH/7*2, HEIGHT/4*3.5, image=self.down, anchor='nw')
        elif (direction == "up"):
            self.up = ImageTk.PhotoImage(file = "up.png")
            self.canvas.create_image(WIDTH/7*3, HEIGHT/4*3.5, image=self.up, anchor='nw')
        elif (direction == "right"):
            self.right = ImageTk.PhotoImage(file = "right.png")
            self.canvas.create_image(WIDTH/7*4, HEIGHT/4*3.5, image=self.right, anchor='nw')

    ## bind the arrow button keys
    def arrowPosition(self):
        self.master.bind('<Left>', self.leftclick)
        self.master.bind('<Down>', self.downclick)
        self.master.bind('<Up>', self.upclick)
        self.master.bind('<Right>', self.rightclick)

    ## Blue arrows: earn 1 point, red arrows: lose 5 points
    ## Left Arrow
    def leftclick(self, event):
        self.canvas.delete(self.dfigure)
        self.dleft = ImageTk.PhotoImage(file = "dleft.png")
        self.dfigure = self.canvas.create_image(WIDTH/4*3+100, HEIGHT/4, image=self.dleft, anchor='nw')
        for arrow in self.arrow_group:
            x = arrow.position()
            if (x[0] == 750.0/7*2 and (x[1] >= 750/4*3.5-60 and x[1] <= 750/4*3.5+60)):
                self.score += 1
                self.update_label()
                self.canvas.after(10, self.flash, "left")
                self.canvas.after(100, self.restore, "left")
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('effect.wav'), maxtime=200)
            rx = arrow.rposition()
            if (rx[0] == 750.0/7*2 and (rx[1] >= 750/4*3.5-60 and rx[1] <= 750/4*3.5+60)):
                self.score -= 5
                self.update_label()
                self.canvas.after(10, self.flash, "left")
                self.canvas.after(100, self.restore, "left")
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('no.wav'), maxtime=200)

    ## Blue arrows: earn 1 point, red arrows: lose 5 points
    ## Down Arrow
    def downclick(self, event):
        self.canvas.delete(self.dfigure)
        self.ddown = ImageTk.PhotoImage(file = "ddown.png")
        self.dfigure = self.canvas.create_image(WIDTH/4*3+100, HEIGHT/4, image=self.ddown, anchor='nw')
        for arrow in self.arrow_group:
            x = arrow.position()
            if (x[0] == 750.0/7*2*2 and (x[1] >= 750/4*3.5-60 and x[1] <= 750/4*3.5+60)):
                self.score += 1
                self.update_label()
                self.canvas.after(10, self.flash, "down")
                self.canvas.after(100, self.restore, "down")
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('effect.wav'), maxtime=200)
            rx = arrow.rposition()
            if (rx[0] == 750.0/7*2*2 and (rx[1] >= 750/4*3.5-60 and rx[1] <= 750/4*3.5+60)):
                self.score -= 5
                self.update_label()
                self.canvas.after(10, self.flash, "down")
                self.canvas.after(100, self.restore, "down")
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('no.wav'), maxtime=200)

    ## Blue arrows: earn 1 point, red arrows: lose 5 points
    ## Up Arrow
    def upclick(self, event):
        self.canvas.delete(self.dfigure)
        self.dup = ImageTk.PhotoImage(file = "dup.png")
        self.dfigure = self.canvas.create_image(WIDTH/4*3+100, HEIGHT/4, image=self.dup, anchor='nw')
        for arrow in self.arrow_group:
            x = arrow.position()
            if (x[0] == 750.0/7*3*2 and (x[1] >= 750/4*3.5-60 and x[1] <= 750/4*3.5+60)):
                self.score += 1
                self.update_label()
                self.canvas.after(10, self.flash, "up")
                self.canvas.after(100, self.restore, "up")
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('effect.wav'), maxtime=200)
            rx = arrow.rposition()
            if (rx[0] == 750.0/7*3*2 and (rx[1] >= 750/4*3.5-60 and rx[1] <= 750/4*3.5+60)):
                self.score -= 5
                self.update_label()
                self.canvas.after(10, self.flash, "up")
                self.canvas.after(100, self.restore, "up")
                pygame.mixer.Channel(6).play(pygame.mixer.Sound('no.wav'), maxtime=200)

    ## Blue arrows: earn 1 point, red arrows: lose 5 points
    ## Right Arrow
    def rightclick(self, event):
        self.canvas.delete(self.dfigure)
        self.dright = ImageTk.PhotoImage(file = "dright.png")
        self.dfigure = self.canvas.create_image(WIDTH/4*3+100, HEIGHT/4, image=self.dright, anchor='nw')
        for arrow in self.arrow_group:
            x = arrow.position()
            if (x[0] == 750.0/7*4*2 and (x[1] >= 750/4*3.5-60 and x[1] <= 750/4*3.5+60)):
                self.score += 1
                self.update_label()
                self.canvas.after(10, self.flash, "right")
                self.canvas.after(100, self.restore, "right")
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('effect.wav'), maxtime=200)
            rx = arrow.rposition()
            if (rx[0] == 750.0/7*4*2 and (rx[1] >= 750/4*3.5-60 and rx[1] <= 750/4*3.5+60)):
                self.score -= 5
                self.update_label()
                self.canvas.after(10, self.flash, "right")
                self.canvas.after(100, self.restore, "right")
                pygame.mixer.Channel(7).play(pygame.mixer.Sound('no.wav'), maxtime=200)

    ## Stop the game
    def quit(self):
        self.quitButton['state'] = Tk.DISABLED
        self.canvas.create_text(WIDTH/2,HEIGHT/2,fill="white",font="Times 100 italic bold",
                                    text="Game Over!")
        self.alive = False

    ## Move the arrow and update the game
    def move(self):
        if self.alive:
            self.arrowPosition()
            
            for arrow in self.arrow_group:
                arrow.arrow_update()
            
            times = SPEED-self.level
            self.master.after(times, self.move)
            
            if self.score == self.level*5:
                self.level += 1
                self.leveluptxt = self.canvas.create_text(WIDTH/2,HEIGHT/2,fill="white",font="Times 100 italic bold", text="Level Up!")
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('cheer.wav'), maxtime=1500)
                self.update_label()
                self.canvas.after(300, self.deletetxt)
            
            if (self.level == 25):
                self.canvas.create_text(WIDTH/2,HEIGHT/2,fill="white",font="Times 100 italic bold",
                                        text="You Won!")
                self.alive = False

            if (self.score < 0):
                self.canvas.create_text(WIDTH/2,HEIGHT/2,fill="white",font="Times 100 italic bold",
                            text="You Lost!")
                self.alive = False

    ## Delete level up text
    def deletetxt(self):
        self.canvas.delete(self.leveluptxt)

##########################################End of ArrowGame####################################################

### main function
def main():
    root = Tk.Tk()
    game = arrowGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
