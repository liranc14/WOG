from games import GuessGame, MemoryGame, CurrencyRoulette
import re




GAMES = {
    1: MemoryGame,
    2: GuessGame,
    3: CurrencyRoulette,
    }


def choose_game():
    game_choose_text = "please choose a game to play:\n"
    for k, v in GAMES.items():
        game_name = " ".join([s for s in re.split("([A-Z][^A-Z]*)", v.__name__) if s])
        game_choose_text += f"{k}: {game_name}\n"

    while True:
        game_id = int(input(game_choose_text))
        if game_id not in GAMES.keys():
            print(f"unknown game, please choose a number from {list(GAMES.keys())}\n")
        else:
            return game_id


if __name__ == '__main__':
    game_id = choose_game()
    game = GAMES[game_id]()
    game.play()