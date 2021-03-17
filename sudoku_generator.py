import turtle
from random import randint, shuffle
from time import sleep
from PIL import Image

difficiult = 5
total_sudokus = 4

for k in range(total_sudokus):
  # Inicializando com uma grade de 9 x 9
  grid = []
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

  myPen = turtle.Turtle()
  myPen._tracer(0)
  myPen.speed(0)
  myPen.color("#000000")
  myPen.hideturtle()
  topLeft_x=-200
  topLeft_y=200

  def text(message,x,y,size):
      FONT = ('Arial', size, 'normal')
      myPen.penup()
      myPen.goto(x,y)    		  
      myPen.write(message,align="left",font=FONT)

  # Desenhando a grade
  def drawGrid(grid):
    intDim=50
    for row in range(0,10):
      if (row%3)==0:
        myPen.pensize(3)
      else:
        myPen.pensize(1)
      myPen.penup()
      myPen.goto(topLeft_x,topLeft_y-row*intDim)
      myPen.pendown()
      myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    for col in range(0,10):
      if (col%3)==0:
        myPen.pensize(3)
      else:
        myPen.pensize(1)    
      myPen.penup()
      myPen.goto(topLeft_x+col*intDim,topLeft_y)
      myPen.pendown()
      myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

    for row in range (0,9):
        for col in range (0,9):
          if grid[row][col]!=0:
            text(grid[row][col],topLeft_x+col*intDim+17,topLeft_y-row*intDim-intDim+6,26)


  # Checando se a grade está completa
  def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
          if grid[row][col]==0:
            return False  
    return True 

  #Função recursiva para checar todas as possibilidades
  def solveGrid(grid):
    global counter
    for i in range(0,81):
      row=i//9
      col=i%9
      if grid[row][col]==0:
        for value in range (1,10):
          if not(value in grid[row]):
            if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
              square=[]
              if row<3:
                if col<3:
                  square=[grid[i][0:3] for i in range(0,3)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(0,3)]
                else:  
                  square=[grid[i][6:9] for i in range(0,3)]
              elif row<6:
                if col<3:
                  square=[grid[i][0:3] for i in range(3,6)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(3,6)]
                else:  
                  square=[grid[i][6:9] for i in range(3,6)]
              else:
                if col<3:
                  square=[grid[i][0:3] for i in range(6,9)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(6,9)]
                else:  
                  square=[grid[i][6:9] for i in range(6,9)]
              if not value in (square[0] + square[1] + square[2]):
                grid[row][col]=value
                if checkGrid(grid):
                  counter+=1
                  break
                else:
                  if solveGrid(grid):
                    return True
        break
    grid[row][col]=0  

  numberList=[1,2,3,4,5,6,7,8,9]
  #shuffle(numberList)

  # Função recursiva para preencher a grade
  def fillGrid(grid):
    global counter
    for i in range(0,81):
      row=i//9
      col=i%9
      if grid[row][col]==0:
        shuffle(numberList)      
        for value in numberList:
          if not(value in grid[row]):
            if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
              square=[]
              if row<3:
                if col<3:
                  square=[grid[i][0:3] for i in range(0,3)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(0,3)]
                else:  
                  square=[grid[i][6:9] for i in range(0,3)]
              elif row<6:
                if col<3:
                  square=[grid[i][0:3] for i in range(3,6)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(3,6)]
                else:  
                  square=[grid[i][6:9] for i in range(3,6)]
              else:
                if col<3:
                  square=[grid[i][0:3] for i in range(6,9)]
                elif col<6:
                  square=[grid[i][3:6] for i in range(6,9)]
                else:  
                  square=[grid[i][6:9] for i in range(6,9)]
              if not value in (square[0] + square[1] + square[2]):
                grid[row][col]=value
                if checkGrid(grid):
                  return True
                else:
                  if fillGrid(grid):
                    return True
        break
    grid[row][col]=0             
      
  # Gerando uma grade completa resolvida
  fillGrid(grid)
  drawGrid(grid)
  myPen.getscreen().update()
  myPen.getscreen().getcanvas().postscript(file = 'resolucao'+str(k+1)+'.ps')
  psimage=Image.open('resolucao'+str(k+1)+'.ps')
  psimage.save('resolucao'+str(k+1)+'.png')
  sleep(1)


  # Removendo números para gerar o jogo

  # Quanto maior o número da dificuldade, mais números serão removidos, tornando o jogo mais difícil
  attempts = difficiult 
  counter=1
  while attempts>0:
    row = randint(0,8)
    col = randint(0,8)
    while grid[row][col]==0:
      row = randint(0,8)
      col = randint(0,8)
    backup = grid[row][col]
    grid[row][col]=0
    
    copyGrid = []
    for r in range(0,9):
      copyGrid.append([])
      for c in range(0,9):
          copyGrid[r].append(grid[r][c])
    
    counter=0      
    solveGrid(copyGrid)   
    
    if counter!=1:
      grid[row][col]=backup
      attempts -= 1
    
    myPen.clear()
    drawGrid(grid) 
    myPen.getscreen().update()
    myPen.getscreen().getcanvas().postscript(file = 'sudoku'+str(k+1)+'.ps')
  
  psimage=Image.open('sudoku'+str(k+1)+'.ps')
  psimage.save('sudoku'+str(k+1)+'.png')
  myPen.clear()