class Book:
  def __init__(self):
    self.title = ''
    self.author = ''
    self.poem_list = []

class Poem:
  def __init__(self,title,dedicatee,lines):
    self.title = title
    self.dedicatee = dedicatee
    self.lines = lines
