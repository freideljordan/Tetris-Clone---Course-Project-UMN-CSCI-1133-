import turtle, random


# I implemented The different Tetrominoes and the Drop function



SCALE = 32 #Controls how many pixels wide each grid square is


class Square(turtle.Turtle):

    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)

class Block:
    def __init__(self):
        self.squares = []
        num = random.randint(1,7)
        if num == 1:
            square1 = Square(3, 21, 'cyan')
            square2 = Square(4, 21, 'cyan')
            square3 = Square(5, 21, 'cyan')
            square4 = Square(6, 21, 'cyan')
        elif num == 2:
            square1 = Square(4, 22, 'blue')
            square2 = Square(4, 21, 'blue')
            square3 = Square(5, 21, 'blue')
            square4 = Square(6, 21, 'blue')
        elif num == 3:
            square1 = Square(3, 21, 'orange')
            square2 = Square(4, 21, 'orange')
            square3 = Square(5, 21, 'orange')
            square4 = Square(5, 22, 'orange')
        elif num == 4:
            square1 = Square(4, 22, 'yellow')
            square2 = Square(4, 21, 'yellow')
            square3 = Square(5, 21, 'yellow')
            square4 = Square(5, 22, 'yellow')
        elif num == 5:
            square1 = Square(3, 21, 'green')
            square2 = Square(4, 21, 'green')
            square3 = Square(4, 22, 'green')
            square4 = Square(5, 22, 'green')
        elif num == 6:
            square1 = Square(3, 21, 'purple')
            square2 = Square(4, 21, 'purple')
            square3 = Square(5, 21, 'purple')
            square4 = Square(4, 22, 'purple')
        elif num == 7:
            square1 = Square(3, 22, 'red')
            square2 = Square(4, 22, 'red')
            square3 = Square(4, 21, 'red')
            square4 = Square(5, 21, 'red')
                

        
        self.squares.append(square1)
        self.squares.append(square2)
        self.squares.append(square3)
        self.squares.append(square4)

    def move(self, dx, dy):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            square.goto(new_x, new_y)

    def valid(self, dx, dy, board):
        for square in self.squares:
            new_x = square.xcor() + dx
            new_y = square.ycor() + dy
            if new_x < 0 or new_x > 9 or new_y < 0 or not board[new_y][new_x]:
                return False
            
        
        return True
    










class Game:
    def __init__(self):

        self.board = [[True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True] ]
    

        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        
        self.active = Block()
        

        
        turtle.ontimer(self.gameloop, 300)

        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.drop, 'Down')

        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()

    


    def gameloop(self):
        if Block.valid(self.active,0, -1, self.board):

            self.active.move(0,-1)
        else:
            for square in self.active.squares:
                self.board[square.ycor()][square.xcor()] = False
            new_block = Block()
            self.active = new_block
        turtle.update()
        turtle.ontimer(self.gameloop, 300)
        
            

    def move_left(self):
        if Block.valid(self.active, -1, 0, self.board):
            self.active.move(-1,0)
            turtle.update

    def move_right(self):
        if Block.valid(self.active, 1, 0, self.board):           
            self.active.move(1,0)
            turtle.update

    def drop(self):
        count = -1
        not_placed = True
        while not_placed:
            if self.active.valid(0, count, self.board):
                count -= 1
            else: 
                self.active.move(0, count+1)
                turtle.update()
                not_placed = False


            

    
        

if __name__ == '__main__':
    Game()



       

        

