import random

class Bird:
    def __init__(self):
        self.posX = random.randint(1,10)
        self.posY = random.randint(1,10)
            

class Pig:
    def __init__(self):
        self.posX = random.randint(1,10)
        self.posY = random.randint(1,10)


class Board:
    def __init__(self):
        self.game_board = '' 
        self.bird = Bird()
        self.pig = Pig()

        # While loop to make sure the bird and pig isn't initialized on the same position
        while True:
            if self.bird.posX == self.pig.posX and self.bird.posY == self.pig.posY:
                self.bird = Bird()
                self.pig = Pig()
            else:
                break
    

    def create_board(self):
        gameboard = ''
        # Two nested for loops - one for each axis
        # The y ranges from 10 to 0, and are decrementing with one for each iteration
        for y in range(10,0,-1): # y akse
            for x in range(1,11,1): # x akse
                # In the nested for loop i check if the position of the bird or pig matches 
                # the iterations in the loops, and if it does, a letter for the animal is printed
                if y == self.bird.posY and x == self.bird.posX:
                    gameboard += 'B  ' 
                elif y == self.pig.posY and x == self.pig.posX:
                    gameboard += 'P  '
                else: gameboard += '*  '
            gameboard += '\n'
        self.game_board = gameboard
    
    def display_board(self):
        print(self.game_board)

    def isGameCompleted(self):
            if self.bird.posX == self.pig.posX and self.bird.posY == self.pig.posY:
                print('Congratulations you\'ve killed the pig')
                return True
            else:
                #print('You haven\'t killed the pig yet! Keep on going!')
                return False

    def move_bird(self, game):
            user_input = input('Make your move: ').lower()

            if user_input == 'w': # move up
                self.bird.posY += 1
            elif user_input == 'a': # move left
                self.bird.posX -= 1
            elif user_input == 'd': # move right
                self.bird.posX += 1
            elif user_input == 's': # move down
                self.bird.posY -= 1
            elif user_input == 'm': # display map
                self.create_board()
                self.display_board()
            else:
                print('Invalid input')
            game.game_over = self.isGameCompleted()

    

    

class Workspace:

    def __init__(self):
        game_over = False
    
    def welcome(self):
        print('\nAngry Birds game instructions:')
        print('Kill the pig by moving the bird on top of it on the board below')
        print('Press w to move upwards')
        print('Press a to move left - Press d to move right') 
        print('Press s to move downwards')
        print('Press the return key between each move')
        print('Press m to use the map as help\n')


class Game:

    def __init__(self):
        self.board = Board()
        self.workspace = Workspace()
        self.game_over = False

    def run(self):
        self.board.create_board()
        self.workspace.welcome()
    
        self.board.display_board()
    
        while self.game_over == False:
            self.board.move_bird(self)

game = Game()
game.run()
