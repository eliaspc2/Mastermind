"""Mastermind"""

from __future__ import annotations

import random


DEFAULT_NUMBERS = 5
MIN_NUMBER = 0
MAX_NUMBER = 10
MAX_ATTEMPTS = 10


class RandomOrder:
    """Gera e avalia uma sequência aleatória de números."""

    def __init__(self, numbers: int = DEFAULT_NUMBERS) -> None:
        # Guarda quantos números vão existir na sequência secreta.
        self.numbers = numbers

    def shuffle(self) -> list[int]:
        """Cria uma sequência aleatória com repetição."""
        # Gera a sequência secreta do jogo.
        return [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(self.numbers)]

    def guess(self, guess: list[int], sequence: list[int]) -> tuple[int, int]:
        """Compara a adivinha com a sequência e devolve números errados/certos e posições certas."""
        # Conta quantos números estão certos na posição certa.
        correct_positions = sum(1 for g, s in zip(guess, sequence) if g == s)
        # Conta quantos números existem na sequência, mesmo que estejam noutra posição.
        total_correct_numbers = sum(min(guess.count(n), sequence.count(n)) for n in set(guess))
        # Remove os que já estão na posição certa para ficar só com os fora de posição.
        correct_wrong_position = total_correct_numbers - correct_positions
        return correct_wrong_position, correct_positions


class Menu:
    """Responsável pela apresentação e navegação nos menus."""

    def menu_inicial(self) -> None:
        # Mostra o menu principal até o utilizador escolher sair.
        while True:
            print("\n=== Mastermind ===")
            print("1 - Jogar")
            print("0 - Sair")
            option = input("Escolha uma opção: ").strip()

            if option == "1":
                # Começa uma nova partida.
                self.menu_jogo()
            elif option == "0":
                print("Saindo do jogo...")
                return
            else:
                print("Opção inválida. Tente novamente.")

    def menu_jogo(self) -> None:
        # Lê o tamanho da sequência, usando o valor por defeito se o utilizador carregar Enter.
        numbers = self.read_positive_int(
            f"Quantos números queres jogar ({DEFAULT_NUMBERS})? ",
            default=DEFAULT_NUMBERS,
        )
        if numbers is None:
            return

        # Cria o jogo e gera a sequência secreta.
        game = RandomOrder(numbers)
        sequence = game.shuffle()

        # Dá ao utilizador um número limitado de tentativas.
        for attempt in range(1, MAX_ATTEMPTS + 1):
            print(f"\nTentativa {attempt} de {MAX_ATTEMPTS}")
            if self.menu_adivinha(game, sequence):
                print("Parabéns! Adivinhaste a sequência.")
                return

        # Mostra a solução quando o jogador falha todas as tentativas.
        print(f"Fim do jogo. A sequência era: {sequence}")

    def menu_adivinha(self, game: RandomOrder, sequence: list[int]) -> bool:
        # Pede a tentativa do jogador.
        print(
            "Tenta adivinhar a sequência de números "
            f"({MIN_NUMBER}-{MAX_NUMBER}, pode haver repetidos)."
        )
        guess = self.read_guess(len(sequence))
        if guess is None:
            return False

        # Compara a tentativa com a sequência secreta.
        correct_wrong_position, correct_positions = game.guess(guess, sequence)
        print(f"Números certos mas na posição errada: {correct_wrong_position}")
        print(f"Números certos na posição certa: {correct_positions}")
        return correct_positions == len(sequence)

    @staticmethod
    def read_positive_int(prompt: str, default: int) -> int | None:
        """Lê um inteiro positivo, usando um valor predefinido se o utilizador carregar Enter."""
        try:
            # Aceita Enter para usar o valor por defeito.
            raw_value = input(prompt).strip()
            value = default if raw_value == "" else int(raw_value)
        except ValueError:
            print("Tem de ser um número inteiro.")
            return None

        # Garante que o número faz sentido para o jogo.
        if value <= 0:
            print("Tem de ser um número maior que zero.")
            return None

        return value

    @staticmethod
    def read_guess(expected_size: int) -> list[int] | None:
        """Lê e valida a tentativa do utilizador."""
        try:
            # Converte a resposta em lista de inteiros.
            guess_input = input("Escreve os números separados por espaços: ").strip()
            guess = [int(x) for x in guess_input.split()]
        except ValueError:
            print("Tem de escrever apenas números inteiros.")
            return None

        # A tentativa tem de ter o mesmo tamanho da sequência secreta.
        if len(guess) != expected_size:
            print(f"A tentativa tem de ter exatamente {expected_size} números.")
            return None

        return guess


def main() -> None:
    """Arranque principal da aplicação."""
    # Inicia o menu principal do jogo.
    Menu().menu_inicial()


if __name__ == "__main__":
    main()
