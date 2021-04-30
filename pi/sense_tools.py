import copy

class Sense_BOARD():
  def __init__(self, hat):
    self.hat = hat
    self.board = []
    self.tempboard = []

    for i in range(8):
      self.board.append([])
      self.tempboard.append([])
      for j in range(8):
        self.board[i].append([0,0,0])
        self.tempboard[i].append([0,0,0])

  def return_board(self):
    return self.board
  
  def print_board(self):
    print(self.board)

  #change the value in tempboard to the pixel value you want
  def set_pixel(self, x, y, c):
    self.tempboard[copy.deepcopy(x)][copy.deepcopy(y)] = c.copy()


  #works with simple bounce.py example
  #loops through all rows and each pixel in row
  #sets a pixel on sense hat if there is a difference between the current board and previous board at that pixel
  def update_board(self):
    for i in range(8):
      for j in range(8):
        if self.tempboard[i][j] != self.board[i][j]:
          self.hat.set_pixel(i,j,self.tempboard[i][j])
          self.board[i][j] = copy.deepcopy(self.tempboard[i][j])
