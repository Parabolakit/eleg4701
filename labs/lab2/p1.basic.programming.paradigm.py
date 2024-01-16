# A. Process oriented programming

def main():
    # the flow chart is always:
    # do [action] to [sth] 
    open_fridge()
    let_in(elephant_data)
    close_fridge()




# B. Object oriented programming 
class BaseFridge:
    def _init_():
        self.container = []
    def _open(self):
        pass
    def _close(self):
        pass
    def put(self, target):
        self.open()
        self.container.append(target)
        self.close()
        
class Siemens(BaseFridge):
    pass

class Midea(BaseFridge):
    pass

class Animal:
    pass

class Lion(Animal):
    pass

class Elephant(Animal):
    pass

def main():
    # in this case,
    # The fridge can hide thier open, and close fucntion
    # Besdies, you can made many different fridge, and all of them can do the same things.
    e = Siemens() #or Midea()
    e.put(Elephant())
