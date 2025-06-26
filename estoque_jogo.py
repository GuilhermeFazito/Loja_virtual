from time import sleep

def menu_loja_jogo():
    while True:
        print("""
=========================================
    Bem vindo ao nosso estoque
       Escolha a Plataforma
========================================
              
1) STEAM
2) PS4/PS5
3) XBOX
4) Outros
5) Carrinho
5) Voltar
 """)
        escolha_plataforma = int(input("Digite sua escolha de 1 a 5: "))

        if escolha_plataforma == 1:
            menu_steam()
        sleep(100)





# criação da area do estoque da STEAM
def menu_steam():

        #Dicionario do carrinho que vai retornar o valor pra função
    carrinho = {}
    
        # Dicionario que contem todos os jogos disponiveis                                
    dicionario_jogos_steam = {
        1: {"nome": "Black Myth: Wukong", "preco": 199.00},
        2: {"nome": "Elden Ring", "preco": 249.90},
        3: {"nome": "FIFA 25", "preco": 299.00},
        4: {"nome": "The Last of Us Part II", "preco": 229.90},
        5: {"nome": "Cuphead + DLC", "preco": 49.99}
        }
    


    
        #Esse while exibe a parte que mostra os jogos disponiveis, e adiciona no carrinho 
    while True:
        print("""
    ========================================
            Estoque da Steam
            O que você deseja?
    ========================================
    """)
        
        # Exibe os jogos disponiveis
        print("📦 Estoque de Jogos:")
        print ("=" * 30)
        for id_jogo, info in dicionario_jogos_steam.items():
            print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
        print("-" * 30)
        print("Caso queira voltar, digite 'EXIT'")

        # Escolha dos jogos que vai adicionar no carrinho
        escolha_jogos = input("Digite o ID do jogo que deseja adicionar no carrinho: ")
        try:
            if escolha_jogos.upper() == "EXIT":
               break
            
            id_jogo = int(escolha_jogos)
            if id_jogo in dicionario_jogos_steam:                           # Verifica se o ID que a pessoa digitou esta no dicionarios dos jogos
                carrinho[id_jogo] = dicionario_jogos_steam[id_jogo]         #Adicionando o a lista do jogo completa(ID_jogo, nome, preço) 
                print(f"⏳ Adicionando jogo ao carrinho")
                sleep(3)
                print(f"✅ {dicionario_jogos_steam[id_jogo]["nome"]} adicionado ao carrinho")

                    #Oferece a opção de escolher outro jogo, rodandno tudo novamento    
                opcao_outro_jogo = input("Deseja escolher outro jogo? ").upper()
                try:
                    if opcao_outro_jogo == "SIM" or opcao_outro_jogo == "S":
                        continue
                    elif opcao_outro_jogo == "NÃO" or opcao_outro_jogo == "NAO" or opcao_outro_jogo == "N":
                        
                        break
                    else:
                         print("Valor invalido, Retornando ao menu Steam, caso queira adicionar mais jogos.")
                         sleep(3)
                except ValueError:
                    print("Valor invalido, Retornando ao menu Steam")
            else:
                print("❌ Escolha invalida. Digite o numero correspondente ao ID do jogo.")
        except ValueError:
            print("❌ Escolha invalida. Digite o numero correspondente ao ID do jogo.")
    
   ## obs: tirar de dentro dessa função e criar outra pra ver o carrinho da steam
    #ofere a escolha de ver oq ela selecionou no carrinho e volta pro menu de estoque 
    
    escolha_ver_carrinho_steam = input("Deseja ver seu carrinho da steam antes de voltar ?").upper()
    try:
        if escolha_ver_carrinho_steam == "SIM" or escolha_ver_carrinho_steam == "S":
                print("\n🛒 Seu Carrinho:")
                print("=" * 40)
                total = 0
                for id_jogo, info in carrinho.items():
                    print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
                    total += info['preco']
                print("=" * 40)
                print(f"💰 Total: R$ {total:>7.2f}")
            
        elif escolha_ver_carrinho_steam == "NAO" or escolha_ver_carrinho_steam == "NÃO" or escolha_ver_carrinho_steam == "N": 
            print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")
            
    except ValueError:
        print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")

    


menu_loja_jogo()