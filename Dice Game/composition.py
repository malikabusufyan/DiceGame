class Die:
    def __init__(self, value):
        self.value = value
 
class Player:
    def __init__(self):
        # Create the instance of Die inside the instance of Player. 
        # This particular Die instance cannot exist without the Player instance that contains it. 
        self.die = Die(5)
 
        
my_player = Player()