

class WOG():

    def __init__(self) -> None:
        self.welcome()
        self.difficulties = [1, 2, 3, 4, 5]
        self.choose_difficulty()


    def welcome(self):
        name = input("name: \n")
        greeting_message = f"Hello {name} and welcome to the World of Games (WoG)\nHere you can find many cool games to play\n"
        print(greeting_message)
        self.player = name


    def choose_difficulty(self):

        while True:
            game_difficulty = int(input("Please choose game difficulty from 1 to 5: \n"))
            if game_difficulty not in self.difficulties:
                print(f"unknown difficulty, please choose a number from {self.difficulties}\n")
            else:
                self.difficulty = game_difficulty
                break

    def end_game(self):
        if self.result:
            print("you won!\n")
        else:
            print("you lost!\n")
        

