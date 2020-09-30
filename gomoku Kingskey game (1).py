'''Name: Kingsley N Okeke
Gomoku is an abstract strategy board game played between two players. A game is won if a chain of five stones is formed(diagonally,
vertically or horizontally). This program implements this game on a 2-d board and also checks if the stones are formed in any particular chain
The maximum board size for this game is 10 * 10.
'''
import random



def print_board():
     '''
     Function to print the gomoku board
     where the game is played and where
     the users' board positions also appear
     '''
     
     print('   ',end='')   
     for z in range(1, column+1): 
          print(z, end=' ') 
     print('   ')
     print('  ', end ='')
     print("+-" * (column)+ '+')

    
     
      #loops through the rows and the columns and prints the board
     for i in range(row): 
          if i+1==10: 
               print(i+1, end ='', sep="")
          else:
               print(i+1, ' ' , end ='', sep="")
                                                       
          for j in range(column):
               print('|', end ='')
               print(board[i][j], end = '')
          print('|')
          print(' ', end =' ')
          print("+-" * (column)+ '+') 

          

def quality_check(inpt):
     """
     This function is a check function that simply inspects
     if a user's input is above the board capacity
     :param inpt: the positive integer or size of a
     particular row or column
     """
     
     if (inpt == '1' or inpt == '2' or inpt == '3' or inpt == '4' or inpt == '5' or inpt == '6' or inpt == '7' or inpt == '8' or inpt == '9' or inpt == '10' ):#if statement to check if the rows inputed is less than or equal to 10  
          return True
     else:
          return False 



def Human_turn():
     ''' This function prompts the user to choose a particular
         position in the board and inspects if the user's input
         is between zero and size of row or size of column
         The human(user) is represented by the character, 'O'. Any position
         chosen by the human is placed with 'O'.
         '''
          

     print('===============')
     print('Human"s Turn')
     print('===============')
     
     while(True):
          while(True):
               A = input('the row where you want your stones between 1 and' + '' + str(row) + ':' )
               if quality_check(A):
                    A = int(A)
               if(int(A)<=row and int(A)>0):
                    break
               print('Wrong Input')

          while(True):
               B = input('the column where you want your stones between 1 and' + '' + str(column) + ':' )
               if quality_check(B):
                    B = int(B)
                    if(B<=column and B>0):
                         break
          if(board[A-1][B-1]==' '):
               board[A-1][B-1] = 'O'
               break
          print("The spot",(A,B) ,  "is already filled")
     print_board()
     winner = Check_Connected_num(A-1,B-1,'O')
     return winner

def Random_Machine_Turn():
     '''This function is the easy mode of the game. It simply prompts the computer to
        place the stone, 'X', on a random spot using the random function.'''
     
     while(True):
          x = input("Enter 'c' to continue")
          if x != 'c':
               print("Enter 'c' to continue again!!")
               continue
          A = random.randint(1,row)
          B = random.randint(1,column)
          if board[A-1][B-1] == ' ': 
               board[A-1][B-1] = 'X' 
               print("===============\nRandom Machine's Choice is {},{}\n===============".format(A,B))
               break
          print("The Spot is already filled")
   
     print_board()

     winner = Check_Connected_num(A-1,B-1,'X')
     return winner


def All_Spots_Chosen():
     
     '''This function checks if there is any spot left in the board.
        It determines if the game would end in stalemate'''
        
     for i in board:
          if ' ' in i: #if statement checks for an empty spot in the board
               return 0 #returns False
     return 1#returns True


def Row_check(x, y,stone):
     '''The row check function checks if there is any winner in the
        game. It does this by going through every column in a particular
        row and checks if there is a chain of stones horizontally'''
     
     p=1
     for i in range(y+1,column):
        if board[x][i] == stone:
             p+=1
        else:
            break
     for j in range(y-1, -1, -1):
        if board[x][j] ==stone:
            p+=1
        else:
            break
     return p


def Column_check(x,y,stone):
     '''The column check function checks if there is any winner in the game.
        It does this by going through every row in a particular column and checks
        if there is a chain of stomes horizontally'''
     
     p =1
     for i in range(x+1, row,1):
          board[i][y]
          if board[i][y]==stone:
               p+=1
          else:
               break
     for j in range(x-1,-1,-1):
          if board[j][y] == stone:
               p+=1
          else:
               break
     return p
def Right_Diagonal_check(x,y,stone):
     '''The right diagonal check function checks if there is any winner in the game.
        It does this by starting at a particular point and proceding to the left part of the board diagonally.
        It checks if there is a chain of stones in this region. '''
     
     p = 1
     i = x
     j = y
     while(i < row -1 and y >0):
          i += 1
          j -= 1
          if(board[i][j] == stone):
            p += 1
          else:
            break
     i = x
     j = y
     while(j<column -1 and i>0):
        i -= 1
        j += 1
        if(board[i][j] == stone):
            p +=1
        else:
            break
     return p
     

def Left_Diagonal_check(x,y,stone):
     '''The left diagonal check function checks if there is any winner in the game.
        It does this by starting at a particular point and proceding to the right part of the board diagonally.
        It checks if there is a chain of stones in this region.'''
     i = x 
     j = y 
    
     p = 1
     while( j>0 and i >0 ):
         i -= 1  #-1 : 4 4 -2:3 3 -3: 2 2 -4: 1 1 
         j -= 1
         if(board[i][j] == stone):
             p += 1
         else:
             break
     i = x 
     j = y 
     while(j<column -1 and  i < row-1):
         j += 1
         i += 1
         if(board[i][j] == stone):
             p += 1
         else:
             break
     return p
     

def Check_Connected_num(input_row, input_col,stone):
    
     Connected_num = Row_check(input_row, input_col,stone)
     if(Connected_num>=5):
          return True
     Connected_num = Column_check(input_row, input_col,stone)
     if(Connected_num>=5):
          return True
     Connected_num=Right_Diagonal_check(input_row,input_col,stone)
     if(Connected_num>=5):
          return True
     Connected_num=Left_Diagonal_check(input_row,input_col,stone)
     if(Connected_num>=5):
          return True
     return False

def Smart_Machine_Turn():
     '''This is the Hard Mode of the game. The computer uses a strategy to always choose the best possible
        spot to  place its stone, 'X'. It considers all four rotations of the board(vertical, horizontal, right
        diagonal, left-diagonal) and checks how many human stones are in each position. The rotation with most number of stones
        is stopped from reaching its maximum of five stones'''

     while('False'):
          c=input("Press 'c' to continue for machine's turn ")
          if c != 'c':
               c=input("Press 'c' key if you want machine to choose a random spot again!! ")
          else:
               break
               
          
          
     max_value = 0
     max_x = -1
     max_y = -1
     for i in range(row):
          for j in range(column):
               if board[i][j] in ' ':
                    row_count = Row_check(i,j,'O')
                    if(row_count > max_value):
                         max_value = row_count
                         max_x = i
                         max_y = j
                    col_count = Column_check(i,j,'O')
                    if(col_count > max_value):
                         max_value = col_count
                         max_x = i
                         max_y = j
                    rdiagonal_count = Right_Diagonal_check(i,j,'O')
                    if(rdiagonal_count >max_value):
                         max_value = rdiagonal_count
                         max_x = i
                         max_y = j
                    
                    ldiagonal_count = Left_Diagonal_check(i,j,'O')
                    if(ldiagonal_count > max_value):
                         max_value = ldiagonal_count
                         max_x = i
                         max_y = j
                    
     board[max_x][max_y] = 'X'
     print("===============\nSmart Machine's Choice is {},{}\n===============".format(max_x+1,max_y+1))
                    
     print_board()
     winner = Check_Connected_num(max_x,max_y,'X')
     return winner 


while(True):
     row = input('Input number of rows that you want from 1-10 ')
     if quality_check(row):  
          row = int(row)
          if(row<11 and row>0):
               break
     print('Wrong Input')
while(True):
     column = input('Input number of columns that you want from 1-10 ') 
     if quality_check(column):
          column = int(column)
          if(column<11 and column>0):
               break
     print('Wrong Input')
choice = [0]
def Choice():
     '''A simple function that prompts the user to select which part of the machine he or she wishes to play with'''
     while('True'):
          choice[0] = input("Who do you want to play with? 1.Random machine 2. Smart machine: ")
          if 0<len(choice[0])<2 and choice[0] in '12':
               choice[0] = int(choice[0])
               break
          
Choice()

     
board = [[' ']*column for i in range(row)]
print_board()

while(True):
     winner = Human_turn() 
     if winner == True:
        print("*******************\nCongrats!!! Human won\n*****************")
        break
     if(All_Spots_Chosen()):
          print("*************************")
          print("No more spot left. Game Ended.")
          print("*************************")
          break
     
     if choice[0] == 1:
        winner = Random_Machine_Turn()
     else:
        winner = Smart_Machine_Turn()
     if winner == True:
        print("*******************\nCongrats!!! Machine won\n*****************")
        break
    
     if(All_Spots_Chosen()):
          print("*************************")
          print("No more spot left. Game Ended.")
          print("*************************")
          break




