from pickle import TRUE
import random

class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value

class Player:

    def __init__(self, die, is_computer=False):

        self._die = die
        self._is_computer = is_computer
        self._counter = 5

    @property
    def die(self):
        return self._die 
    
    @property
    def is_computer(self):
        self._is_computer

    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter+=1
    
    def decrement_counter(self):
        self._counter-=1
    
    def roll_dice(self):
        return self._die.roll()

class DiceGame:

    def __init__(self, player, computer):
        self._player=player
        self._computer=computer
    
    def play(self):
        print("================================")
        print("***Welcome to Roll the Dice!!***")
        print("================================")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        #Welcome the User
        print("\n------New Round---------")
        input("Please enter any key to roll the dice")

        #Roll The Dice
        player_value = self._player.roll_dice()
        computer_value = self._computer.roll_dice()

        #show the values
        print(f"Your Die: {player_value}")
        print(f"Computer Die: {computer_value}")

        #Determine Winner or Loser
        if player_value>computer_value:
            print("Congratulations!! You Won the Round")
            self._player.decrement_counter()
            self._computer.increment_counter()

        elif player_value<computer_value:
            print("The Computer Won this Round!! Try Again")
            self._computer.decrement_counter()
            self._player.increment_counter()
        
        else:
            print("It's a Tie!!!")

        #Show Counters
        print(f"\nYour Counter: {self._player.counter}")
        print(f"Computer Counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True

        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True

        else:
            return False
    
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n*******Game Over*******")
            print("The Computer Won the Game")
            print("==========================")

        else:
            print("\n*******Game Over*******")
            print("Congratulations!!! You Won the Game")
            print("==========================")
        
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()
