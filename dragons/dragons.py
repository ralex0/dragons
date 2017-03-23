class Dragon(object):
    
    def __init__(self, name, health=10):
        self.name = name
        self.health = health
        
    def roar(self):
        print("{}: Roooooooooar!".format(self.name))
        
    def attack(self, target):
        target.health -= 1
        
        
        
    