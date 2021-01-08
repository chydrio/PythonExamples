class Game:

    def __init__(self):
        self.grid = [['' for x in range(6)]  for y in range(6)]

    def print(self):
        print('    A  ','B  ','C  ','D  ','E  ','F')
        for i in range(len(self.grid)):

            print(i+1, self.grid[i])


    def addBoat(self):
        print("add start Boat: ")
        #A2->0,1 row,col
        coord=input()
        col1=int(coord[1])-1
        if not isValidCoord(coord[0],col1):
            return
        row1=letters_to_numbers[coord[0]]

        #row,col
        print("add end Boat: ")
        coord2=input()
        col2=int(coord2[1])-1
        if not isValidCoord(coord2[0],col2):
            return
        row2=letters_to_numbers[coord2[0]]

        #fill the grid
        #vertical Boat
        if col1==col2:
            for row in range(min(row1,row2),max(row1,row2)+1):
                self.grid[row][col1]="O"
        #horizontal Boat
        elif row1==row2:
            for col in range(min(col1,col2),max(col1,col2)+1):
                self.grid[row1][col]="O"


    def addBomb(self):
        print("add Bomb: ")
        coord=input()
        row=letters_to_numbers[coord[0]]
        col=int(coord[1])-1
        if self.grid[row][col]=="O":
            self.grid[row][col]="X"

    def isGameOver(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col]=="O":
                    return False
        print("Game Over")
        return True

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}

def isValidCoord(row,col):
    if row not in letters_to_numbers or col>5 or col<0:
        print("invalid data")


def main():
    game=Game()
    game.print()
    game.addBoat()
    game.print()
    while(not   game.isGameOver()):
        game.addBomb()
    game.print()
main()
