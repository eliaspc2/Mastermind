"""Objeto para gerir menus da aplicação."""

from .random_order import RandomOrder

class Menu:
    """Responsável pela apresentação e navegação nos menus."""

    def menu_inicial(self):

        while True:
            print("1 - Jogar")
            print("2 - Sair")
            option = input("Escolha uma opção: ")

            if option == "1":
                print("Iniciando o jogo...")
                self.menu_jogo()
            elif option == "2":
                print("Saindo do jogo...")
                exit()
            else:
                print("Opção inválida. Tente novamente.")

    def menu_jogo(self):
        game = RandomOrder(int(input("quantos números queres jogar (4)? ")))
        print(game)
        
        
