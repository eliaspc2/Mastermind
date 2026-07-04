"""Ponto de entrada da aplicação."""

from src.objects.menu import Menu


def main() -> None:
    """Arranque principal da app."""
    print("Mastermind: aplicação pronta para arrancar.")
    game_menu = Menu()
    game_menu.menu_inicial()


if __name__ == "__main__":
    main()
