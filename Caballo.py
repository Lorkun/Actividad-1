# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 12:04:27 2022

@author: Usuario
"""

chessBoard = [[1,2,3],[4,5,6], [7,8,9], [None, 0, None]]

def countMatrizElements(matriz):
 counter = 0
 for row in range(len(matriz)):
  for col in range (len(matriz[row])):
      if matriz[row][col] != None:
          counter = counter + 1
 return counter

def horseValidMovementsAux(board, movements, startpoint):
    if movements == 0:
        return 0
    for row in range(len(board)):
        for col in range (len(board[row])):
            if(board[row][col] == startpoint):
                if(row==0 and col == 0):
                   return 2+horseValidMovementsAux(board,movements-1,board[row+1][col+2])+horseValidMovementsAux(board,movements-1,board[row+2][col+1])
                elif(row==1 and col == 0):
                    return 3+horseValidMovementsAux(board,movements-1,board[row+1][col+2])+horseValidMovementsAux(board,movements-1,board[row-1][col+2])+horseValidMovementsAux(board,movements-1,board[row+2][col+1])
                elif(row==2 and col == 0):
                    return 2+horseValidMovementsAux(board,movements-1,board[row-1][col+2])+horseValidMovementsAux(board,movements-1,board[row-2][col+1])
                elif(row== 3 and col == 1):
                    return 2+horseValidMovementsAux(board,movements-1,board[row-2][col+1])+horseValidMovementsAux(board,movements-1,board[row-2][col-1])
                elif(row==0 and col == 1):
                   return 2+horseValidMovementsAux(board,movements-1,board[row+2][col+1])+horseValidMovementsAux(board,movements-1,board[row+2][col-1])
                elif(row==1 and col == 1):
                    return 0
                elif(row==2 and col == 1):
                    return 2+horseValidMovementsAux(board,movements-1,board[row-2][col+1])+horseValidMovementsAux(board,movements-1,board[row-2][col-1])
                elif(row==0 and col == 2):
                   return 2+horseValidMovementsAux(board,movements-1,board[row+2][col-1])+horseValidMovementsAux(board,movements-1,board[row+1][col-2])
                elif(row==1 and col == 2):
                    return 3+horseValidMovementsAux(board,movements-1,board[row+2][col-1])+horseValidMovementsAux(board,movements-1,board[row-1][col-2])+horseValidMovementsAux(board,movements-1,board[row+1][col-2])
                elif(row==2 and col == 2):
                    return 2+horseValidMovementsAux(board,movements-1,board[row-2][col-1])+horseValidMovementsAux(board,movements-1,board[row-1][col-2])
                                

def horseValidMovements(board, movements):
 countingMovements = 0
 for startPosition in range(countMatrizElements(board)):
   countingMovements = countingMovements + horseValidMovementsAux(board, movements, startPosition)
 return countingMovements

print(horseValidMovements(chessBoard,3))
def horseDef(board, movements):
    n = movements - 1
    a = horseValidMovements(board, movements)
    b = horseValidMovements(board, n)
    c = a-b
    return c
print(horseDef(chessBoard,3))