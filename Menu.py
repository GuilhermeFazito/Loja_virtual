from time import sleep

def menu_principal():
    while True:
        print(f"""
=====================================          
    BEM VINDO A NOSSA LOJA VIRTUAL
=====================================
 O que vc deseja?
 1 -> ...
 2 -> ...
 3 -> ...
 4 -> Saber mais sobre a loja         
 5 -> Sair       
          """)
        try:
            escolha_menu = input(f"Digite aqui alguma opção: ")

            escolha_menu = int(escolha_menu)

            if escolha_menu in [1, 2, 3, 4, 5]:
                return escolha_menu
            else: 
                print(f"\nEssa opção nao existe, ({escolha_menu}) é um numero invalido")
                print(f"Tente novamente.")
                sleep(1)
        except ValueError:
            print(f"\nError, tente apenas numero validos de 1 a 5")
            sleep(1)


