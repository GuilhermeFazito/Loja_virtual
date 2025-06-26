from time import sleep
from random import randint # Será usado em breve tambem

codigo_gift = [''] # Essa lista ainda vai ser mexida, ta ai como exemplo por enquanto

# Função comprar_gift_card() falta terminar!

def menu_carrinho_gift(): # Função para mostrar o menu e fazer os encaminhamentos
    while True:
        print("""
=========================================
      Bem vindo ao nosso estoque de 
              GIFT CARDS!
=========================================
              
 1 -> Comprar Gift Card
 2 -> Ver Saldo
 3 -> Resgatar Código
 4 -> Voltar ao menu principl
 """)
        try:
            opcoes = input("Digite sua escolha de 1 a 5: ")
            
            int_opcoes = int(opcoes)
        
            if int_opcoes in [1, 2, 3, 4, 5]:
                if int_opcoes == 1:
                    comprar_gift_card()
                elif int_opcoes == 2: # Em breve
                    ... 
                elif int_opcoes == 3: # Feito em pedaço, ainda falta terminar
                    sleep(1)
                    resgatar_codigo_gift_card()
                elif int_opcoes == 4: 
                    print(f"\nOk voltando ao menu inicial!")
                    sleep(0.5)
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
     
# Falta terminar essa função
def comprar_gift_card(): # Função de compra de gifts cards, com o menu e as opções integradas na funçao
    while True:
        print(f"""
=========================================                    
--->       Comprar Gift Card         <--- 
              
=========================================                     
 Opções disponíveis:
 1 - R$ 50,00
 2 - R$ 100,00
 3 - R$ 150,00
 4 - R$ 200,00
 5 - Valor Desejado
                      """)
        try:
            valor = input(f"Digite o alguma das opções: ")
            int_valor = int(valor)
            if int_valor in [1, 2, 3, 4, 5]:
                if int_valor == 1:
                    ... # Em breve
                elif int_valor == 2:
                    ... # Em breve
                elif int_valor == 3:
                    ... # Em breve
                elif int_valor == 4:
                    ... # Em breve
                elif int_valor == 5:
                    ... # Em breve
                else:
                    print(f"\nOpção invalida ({int_valor}) Não existe")
        except ValueError:
            print(f"Error, tente apenas numeros validos de 1 a 5")
                    
def resgatar_codigo_gift_card(): # Função para resgatar codigos dos gift cards na loja
    while True:
        print(f"""
=========================================
        RESGATE SEUS CODIGO AQUI!
=========================================
⇓ Exemplo de codigo ⇓
""")
        print("\033[33m (4E5EE-EE45E-E4E4E)\033[0m")
        sleep(0.5)
        codigo = input(f"\nDigite o código do gift card em (MAIUSCULO): ").upper()

        if codigo in codigo_gift:
            print(f"\nResgatado com Sucesso!")
            resposta = retorno()

            if resposta == '':
                continue
            else:
                print('\nOk voltando ao menu principal')
                sleep(0.5)
                break
        else:
            print(f"\nTalvez o codigo {codigo} ja foi usado ou não existe!")
            print(f"\nTente novamente")
            sleep(0.5)

menu_carrinho_gift()