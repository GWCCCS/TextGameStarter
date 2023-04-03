class Character:
    '''Base Character class.  '''
    total_characters = 0
    starting_items = ["sneakers","hat","tunic"] # start with a list.  It might be better to use...
    def __init__(self, initialposition=(0,0)):          
          Character.total_characters = Character.total_characters + 1
          self.position = initialposition 
          self.items = []
          self.items.extend(Character.starting_items)
    
    @property
    def position(self):
        return self.x, self.y
    
    @position.setter
    def position(self,position):
          self.x, self.y = position

    def additem(self, item_):
        self.items.append(item_)

    def removeitem(self, item_):
        self.items.remove(item_)

if __name__ == "__main__":
      tester = Character((1,1))
      tester.position = (2,2)
      print(tester.position)
      tester.additem("shield")
      tester.removeitem("hat")
      print(tester.items)