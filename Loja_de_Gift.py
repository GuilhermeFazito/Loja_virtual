from time import sleep # Para deixar mais responsivo
from random import randint # Será usado em breve tambem

codigo_gift = [] # Essa lista ainda vai ser mexida, ta ai como exemplo por enquanto
carrinho_gift = {} # Carrinho dos gifts cards

def menu_carrinho_gift(): # Função para mostrar o menu e fazer os encaminhamentos
    while True:
        print("""
=========================================
      Bem vindo ao nosso estoque de 
              GIFT CARDS!
=========================================
              
 1 -> Adicionar Gift Card ao Carrinho
 2 -> Ver Carrinho
 3 -> Resgatar Código
 4 -> Voltar ao menu principal
 """)
        try:
            opcoes = input("Digite sua escolha de 1 a 5: ")      # Opçao de escolha
            int_opcoes = int(opcoes)                             # Tipando o input para inteiro para evitar erros
        
            if int_opcoes == 1: # Compra de gifts cards
                comprar_gift_card()
            elif int_opcoes == 2: # Feito em pedaço, ainda falta terminar
                mostrar_carrinho()
            elif int_opcoes == 4:
                print("\nSaindo do menu. Obrigado!")
                sleep(1)
                break 
            else:
                print(f"\nEssa opção nao existe, ({int_opcoes}) é uma opção invalida")
                sleep(0.7)
        
        except ValueError:
            print(f"\nError, Tente apenas numeros validos de 1 a 4")
            sleep(0.7)

def retorno(): # Função de pergunta para a pessoa se ela quer refazer o que estava fazendo
    while True:
     print(f"\nVocê Deseja fazer novamente?") 
     voltar = input(f"Aperte (ENTER) ou digite (NÃO): ").upper().strip()

     if voltar =='':
         print(f"\nOk de novo..")
         sleep(0.5)
         return voltar
     elif voltar == 'NÃO' or 'N' or 'NAO':
        break                 

def comprar_gift_card(): # Função do menu de compra dos gifts cards
    while True:
        print(f"""
=========================================
    Escolha um Gift Card para adicionar 
    ao carrinho.
=========================================     
 1 -> R$ 50
 2 -> R$ 100
 3 -> R$ 150
 4 -> R$ 200
                        """)
        escolha = int(input(f"Digite uma opção: "))

        if escolha == 1:                # Escolhendo os gifts cards
            valor = 'R$ 50'             # Valor do GIFT CARD
        elif escolha == 2:              # Escolhendo os gifts cards
            valor = 'R$ 100'            # Valor do GIFT CARD
        elif escolha == 3:              # Escolhendo os gifts cards
            valor = 'R$ 150'            # Valor do GIFT CARD
        elif escolha == 4:              # Escolhendo os gifts cards
            valor = 'R$ 200'            # Valor do GIFT CARD
        else:
            print(f"Opção invalida")
            continue

        # ADICIONAR AO CARRINHO
        if valor in carrinho_gift:         
            carrinho_gift[valor] += 1
        else:
            carrinho_gift[valor] = 1
        print(f"\n{valor} Adicionado ao carrinho!")
        sleep(0.5)
        
        # TRATAMENTO DE ERRO PARA ESCOLHA DO USUARIO DE COMPRAR NOVAMENTE
        try:
            print(f"\nDeseja adicionar mais gifts cards ao carrinho?")
            
            adiconar_mais = input(f"\n[S]im ou [N]ao: ").upper()

            lista_aprova_de_idiotas = ['NÃO', 'NAO', 'N']  # Lista para validação da escolha (Não)

            if adiconar_mais == 'SIM' or adiconar_mais == 'S':
                print(f"\nVoltando")
            elif adiconar_mais in lista_aprova_de_idiotas:
                print(f"\nOk voltando ao menu principal")
                break
            else:
                print(f"\nOpção invalida")
                sleep(1)
        except ValueError:
            print(f"Error")

def mostrar_carrinho(): # Função para mostrar o carrinho do cliente
    print(f"""
=========================================
             SEU CARRINHO!
=========================================
""")
    # Mostrar o carrinho vazio se nao houver nada
    if not carrinho_gift:
        print(f"Carrinho vazio!")
    else:
        # Mostrar o carrinho
        for valor, qtd in carrinho_gift.items():                     
            print(qtd,"\033[31mx Gift Card de R$\033[0m", valor)
        sleep(1)

if __name__ == "__main__":
    menu_carrinho_gift()
    comprar_gift_card()