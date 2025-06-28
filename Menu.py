from time import sleep

# O menu que será exibido, se quiser pode acresentar mais opções ou decidir o que vai ter
# nas opções que estao com (...)
def menu_principal():
    while True:
        print(f"""
=======================================          
    BEM VINDO A NOSSA LOJA VIRTUAL
De Gift Card e Jogos em Midia Digital
=======================================
 O que vc deseja?
 1 -> Loja de Jogos
 2 -> Loja de Gift Card
 3 -> ...
 4 -> Saber mais sobre a loja         
 5 -> Sair       
          """)
        # Tratamento de Erro das escolhas, a resposta vai ir para o main onde será feito o encaminhamento,
        # ou vc pode criar um arquivo para fazer isso e so importar o menu()
        try:
            escolha_menu = input(f"Digite aqui alguma opção: ")

            escolha_menu = int(escolha_menu)

            if escolha_menu in [1, 2, 3, 4, 5]:
                if escolha_menu == 5:  
                    pergunta_de_seguranca()
                    continue         
                return escolha_menu
            else: 
                print(f"\nEssa opção nao existe, ({escolha_menu}) é um numero invalido")
                print(f"Tente novamente.")
                sleep(1)
        except ValueError:
            print(f"\nError, tente apenas numero validos de 1 a 5")
            sleep(1)

# Função para perguntar se a pessoa realmente deseja sair!
def pergunta_de_seguranca():
    while True:
        print(f"\nVoce tem certeza fazer isso?")
        escolha_pergunta_de_seguranca = input(f"Digite aqui sua resposta (S/N): ").upper().replace("Ã", "A")

        # Tratamento de Erro, a prova de idiotas!
        try:
            if escolha_pergunta_de_seguranca == 'S' or escolha_pergunta_de_seguranca == 'SIM':
                exit()
            elif escolha_pergunta_de_seguranca == 'N' or escolha_pergunta_de_seguranca == 'NAO':
                print(f"\nOk Voltando ao menu principal")
                sleep(1)
                break
            else:
                print(f"\nDigite apenas S ou N!")
                sleep(0.5)
        except ValueError:
            print(f"\nError, tente apenas -> (S) ou (N)!")



if __name__ == "__main__":
    menu_principal()




