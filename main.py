from time import sleep
from tkinter import Tk, Label

window = Tk()

class Card:
  def __init__(self, text_, x, y):
    self.name = text_
    self.card = Label(window, bg="white", borderwidth=3, relief="raised", width=5, height=2, text=text_, fg="black", padx=20, pady=20)
    self.card.grid(row=x, column=y)
    self.card.bind("<Button-1>", self.pick_up)
    self.card.bind("<B1-Motion>", self.drag)
    self.card.bind("<B1-ButtonRelease>", self.drop)
  def pick_up(self, event):
    item = event.widget
    item.start_x = event.x
    item.start_y = event.y
  def drag(self, event):
    item = event.widget
    x = item.winfo_x() - item.start_x + event.x
    y = item.winfo_y() - item.start_y + event.y
    item.place(x=x, y=y)
  def drop(self, event):
    item = event.widget
    print(item.winfo_x(), item.winfo_y())
  def animate(self):
    print('moving...', self.name) 

cards = [ 'lorem', 'ipsum', 'epsum', 'nislum', 'fizz', 'fuzz', 'buzz', 'foo', 'bar' ]
grid = []
for x in range(3):
  row = []
  x = (x + 1) * 50
  for y in range(3):
    y = (y + 1) * 50 
    row.append([x,y])
  grid.append(row)
# print(grid)

# for num, card in enumerate(cards):
#   x = 50 * num
#   y = 100
#   Card(card, x, y)

for row in grid:
  for column in row:
    x,y = column
    Card(f"{x}_card", x, y) 

window.mainloop()
