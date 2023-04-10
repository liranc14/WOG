from base_game import WOG
import random
from time import sleep
from currency_converter import CurrencyConverter
import os
import platform



class GuessGame(WOG):
    def __init__(self) -> None:
        super().__init__()
        self.generate_number()


    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)


    def get_guess_from_user(self):
        while True:
            user_guess = int(input(f"guess my number between 1 and {self.difficulty}:"))
            if user_guess < 1 or user_guess > self.difficulty:
                print(f"invalid number, please guess a number between 1 and {self.difficulty}:")
            else:
                self.user_guess = user_guess
                break

    def compare_results(self)-> bool:
        return self.user_guess == self.secret_number
    

    def play(self):
        self.get_guess_from_user()
        self.result = self.compare_results()
        self.end_game()

            

class MemoryGame(WOG):
    def __init__(self) -> None:
        super().__init__()
        self.generate_sequence()
        self.show_time = 1
        self.clear_screen = 'cls' if platform.system() == 'Windows' else 'clear'


    def generate_sequence(self):

        self.sequence = []
        for _ in range(self.difficulty):
            self.sequence.append(random.randint(1, 101))



    def get_list_from_user(self):

        print("try to memorize those numbers:")
        print(self.sequence)
        sleep(self.show_time)
        os.system(self.clear_screen)

        print("type one number at a time and press enter to proceed")
        self.users_list = []
        number_chart = {
            1: "st",
            2: "nd",
            3: "rd",
        }
        for i in range(1, self.difficulty + 1):
            
            input_text = f"{str(i)}{number_chart.get(i, 'th')} number:"
            self.users_list.append(int(input(input_text)))


    def is_list_equal(self)-> bool:
        return self.sequence == self.users_list


    def play(self):
        self.get_list_from_user()
        self.result = self.is_list_equal()
        self.end_game()



class CurrencyRoulette(WOG):
    def __init__(self) -> None:
        super().__init__()



    def get_amounts(self):
        self.dollar = random.randint(1, 101)
        c = CurrencyConverter()
        self.shekel = c.convert(self.dollar, 'USD', 'ILS')


    def get_guess_from_user(self):
        self.user_guess = int(input(f"amout in dollar is {self.dollar}, the amount in shekel is: \n"))

    def compare_results(self) -> bool:
        boundary = max(self.difficulties) + 1
        min_boundary = self.shekel - (boundary - self.difficulty)
        max_boundary = self.shekel + (boundary - self.difficulty)
        return self.user_guess >= min_boundary and self.user_guess <= max_boundary


    def play(self):
        self.get_amounts()
        self.get_guess_from_user()
        self.result = self.compare_results()
        self.end_game()