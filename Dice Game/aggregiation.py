class Die:
    def __init__(self, value):
        self.value = value
 
class Player:
    def __init__(self, die):
        self.die = die
 
# Create the simpler object
my_die = Die(5)
 
# Pass that object as argument to the object that will contain it. 
my_player = Player(my_die)        