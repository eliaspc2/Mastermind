"""Mastermind - aplicação principal num único ficheiro."""

import random


class RandomOrder:
    """Gera uma sequência aleatória de números."""

    def __init__(self, numbers: int = 4) -> None:
        self.numbers = numbers

    def shuffle(self) -> list[int]:
        return [random.randint(0, 10) for _ in range(self.numbers)]


class Menu:
    """Responsável pela apresentação e navegação nos menus."""

    def menu_inicial(self) -> None:
        while True:
            print("1 - Jogar")
            print("2 - Sair")
            option = input("Escolha uma opção: ")

            if option == "1":
                print("Iniciando o jogo...")
                self.menu_jogo()
            elif option == "2":
                print("Saindo do jogo...")
                return
            else:
                print("Opção inválida. Tente novamente.")

    def menu_jogo(self) -> None:
        try:
            numbers = int(input("Quantos números queres jogar (4)? ") or 4)
        except ValueError:
            print("Tem de ser um número inteiro.")
            return

        game = RandomOrder(numbers)
        sequence = game.shuffle()
        print(f"Sequência gerada: {sequence}")


def main() -> None:
    """Arranque principal da aplicação."""
    print("Mastermind: aplicação pronta para arrancar.")
    game_menu = Menu()
    game_menu.menu_inicial()


if __name__ == "__main__":
    main()

