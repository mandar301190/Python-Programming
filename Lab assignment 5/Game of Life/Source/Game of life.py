import sys
import turtle       #turtle function is used for graphics purpose such as to draw pattern, initials etc.
import random

CELL_SIZE = 10      #Size of the board will be measured in pixels


class GameofLife:       #Super class defined for game of life. This class will later on called.

    def __init__(self, asize, bsize):       #init constructor is used for defining a and b values

        self.state = set()
        self.asize, self.bsize = asize, bsize

    def legal(self, x, y):

        return (0 <= x < self.asize) and (0 <= y < self.bsize) #It will return true value if x and y values exist on board

    def set(self, x, y):    #Defines a set to the live state

        if not self.legal(x, y):
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                x, y, self.asize, self.bsize))

        presskey = (x, y)
        self.state.add(presskey)

    def makeRandom(self):         #It is used to fill up the board with random pattern in it

        self.erase()
        for i in range(0, self.asize):
            for j in range(0, self.bsize):
                if random.random() > 0.5:
                    self.set(i, j)

    def toggle(self, x, y):       #Used to toggle a state of game between live and dead cells when continuous key pressed

        if not self.legal(x, y):
            raise ValueError("Coordinates for Game are {}, {} Not in range ..{}, ..{}".format(
                x, y, self.asize, self.bsize))
        key = (x, y)
        if key in self.state:
            self.state.remove(key)
        else:
            self.state.add(key)

    def erase(self):        #It is used to delete or clear entire board when erase 'E' key pressed

        self.state.clear()

    def step(self):    #Computes the generation of pixels and updating display upon any key pressed which has been defined above

        z = set()
        for i in range(self.asize):
            x_range = range(max(0, i - 1), min(self.asize, i + 2))
            for j in range(self.bsize):
                s = 0
                live = ((i, j) in self.state)
                for yp in range(max(0, j - 1), min(self.bsize, j + 2)):
                    for xp in x_range:
                        if (xp, yp) in self.state:
                            s += 1


                s -= live     #Substracts central cell value

                if s == 3:     #Used to show birth

                    z.add((i, j))
                elif s == 2 and live:      #Used to show survival

                    z.add((i, j))
                elif live:         #Used to show death

                    pass

        self.state = z


    def draw(self, x, y):   #It is used to update each cell value on display board

        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.color('blue')    #Cell size color as blue
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()

    def display(self):     #Function used to draw whole board

        turtle.clear()
        for i in range(self.asize):
            for j in range(self.bsize):
                self.draw(i, j)
        turtle.update()


def display_ithelp_window():       #window function defines board height and width value as well as display background color
    from turtle import TK          #TK is argument and turtle is function
    root = TK.Tk()
    frame = TK.Frame()
    canvas = TK.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    help_screen = turtle.TurtleScreen(canvas)   #Draws whole canvas
    help_it = turtle.RawTurtle(help_screen)
    help_it.penup()
    help_it.hideturtle()
    help_it.speed('fastest')

    width, height = help_screen.screensize()
    line_itheight = 20
    y = height // 2 - 30
    for s in ("You can click on any cell to make either dead or alive.",
              "Given Keyboard commands are:",        #Defines key commands on board access
              " E)Erase the board",
              " R)Random fill",
              " S)Step once or",
              " C)Continuously -- You can use 'S' to resume further stepping and continue with game",
              " Q)Quit"):
        help_it.setpos(-(width / 2), y)
        help_it.write(s, font=('sans-serif', 14, 'normal'))
        y -= line_itheight


def main():          #Main function is used to call all subclasses in it and pass its arguments
    display_ithelp_window()

    scr = turtle.Screen()
    turtle.mode('standard')   #turtle function will be used to create canvas in standard mode
    xsize, ysize = scr.screensize()
    turtle.setworldcoordinates(0, 0, xsize, ysize)

    turtle.hideturtle()
    turtle.speed('fastest')      #Defines maximum speed on which cells can be toggled
    turtle.tracer(0, 0)
    turtle.penup()

    gameboard = GameofLife(xsize // CELL_SIZE, 1 + ysize // CELL_SIZE)


    def toggle(x, y):   #function used to call toggle of cell
        cell_x = x // CELL_SIZE
        cell_y = y // CELL_SIZE
        if gameboard.is_legal(cell_x, cell_y):
            gameboard.toggle(cell_x, cell_y)
            gameboard.display()


    gameboard.makeRandom()
    gameboard.display()


    def erase():          #Function to erase cells on board
        gameboard.erase()
        gameboard.display()

    turtle.onkey(erase, 'e')           #key to erase the baord

    def makeRandom():    #Function to generate pattern randomly
        gameboard.makeRandom()
        gameboard.display()

    turtle.onkey(makeRandom, 'r')        #Key to get random

    turtle.onkey(sys.exit, 'q')          #key to quit board


    continuous = False

    def step_once():       #Set up keys used to perform generation steps, that would be either one at a time or complete not
        nonlocal continuous
        continuous = False
        perform_step()

    def step_continuous():    # Function to perform continuous generation of pattern
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():       #Function to perform one step at a time
        gameboard.step()
        gameboard.display()

        if continuous:         #If pattern generation is continuous then sets timer to define limit of 25 milliseconds
            turtle.ontimer(perform_step, 25)

    turtle.onkey(step_once, 's')      #For generating one step at a time
    turtle.onkey(step_continuous, 'c')    #For generating continuous pattern


    turtle.listen()
    turtle.mainloop()  #TK main loop


if __name__ == '__main__':    #At end main function as a private would be calledto pass all arguments by sub and super classes
    main()