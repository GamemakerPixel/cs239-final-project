from view.cli import CliView
from model.game import Game


def main():
    game = Game(CliView())
    game.begin()


if __name__ == "__main__":
    main()
