class Game():
    def __init__(self, p1_move=False, p2_move=False):
        self.table = [
            [4,4,4,4,4,4],
            [4,4,20,4,4,4]
        ]
        self.p1_move   = p1_move
        self.p2_move   = p2_move
        self.p1_points = 0
        self.p2_points = 0
    
    #<----- go left when row==0
    #------> go right when row==1
    # when p1 moves give points to p1 when col < 0
    # when p2 moves give to p2 when col == len(table)
    def distribute(self, row, col):
        #check if valid move
        if(row == 1 and self.p2_move or
           row == 0 and self.p1_move):
            stones = self.table[row][col]
            self.table[row][col] = 0
            direction = 1 if row== 1 else -1
            for _ in range(stones):
                #Go to next cell given the direction
                col += direction

                if(col < 0):
                    print('Going Downstairs')
                    row = 1 # go downstairs
                    direction = 1
                    if(self.p1_move):
                        print('Player 1 increased point')
                        print()
                        self.p1_points +=1
                    else:
                        col += direction
                        self.table[row][col] += 1
                        
                elif(col >= len(self.table[0])):
                    print('Going Upstairs')
                    row = 0 #go upstairs
                    direction = -1
                    if(self.p2_move):
                        print('Player 2 increased point')
                        print()
                        self.p2_points +=1
                    else:
                        col += direction
                        self.table[row][col] += 1
                else:
                    self.table[row][col] += 1
            return (row,col)
        else:
            return 'Invalid Move'
    
    def display(self):
        print('Table: ')
        for x in self.table:
            print(x)
        print('Player1 points: ',   self.p1_points)
        print('Player2 points: ',   self.p2_points)
        
        
    

g = Game(p2_move=True)
print('Stopped position: ',g.distribute(1,2))
g.display()

# (0,6) is the stopped position for player 2
# (1,-1)is the stopped position for player 1

#
#
#   [4,4,4,4,4,4]   p1 = 1
#   [4,4,4,4,4,4]
#
#
#









