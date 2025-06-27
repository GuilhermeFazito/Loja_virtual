from time import sleep

# --- Importação dos Dicionários de Jogos ---

# @st_games é o ALIAS para o dicionario_jogos_steam.
from DB.DB_steam_games import dicionario_jogos_steam as st_games

# @ps5_games é o ALIAS para o dicionario_jogos_ps5.
from DB.DB_ps5_games import dicionario_jogos_ps5 as ps5_games

# @xbox_games é o ALIAS para o dicionario_jogos_xbox.
from DB.DB_xbox_games import dicionario_jogos_xbox as xbox_games

# --- Estrutura de Exemplo de um Jogo ---
# As estruturas continuamm a mesma junto com o metodo de implementação.
# As unicas diferenças são os "apelidos" dados para diminuir a verbosidade
# O codigo já foi editado para os apelidos para que não ajá nenhum tipo de erro 
# referente a isso.

# --- Observações ---
# Os aliases (st_games, ps5_games, xbox_games) são usados para diminuir
# a verbosidade e facilitar a referência aos dicionários de jogos
# em outras partes do código.


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
        elif escolha_plataforma == 2:
            menu_ps4()
        




# criação da area do estoque da STEAM
def menu_steam():

        #Dicionario do carrinho que vai retornar o valor pra função
    carrinho_steam = {}

    # FELIPE -> Criei um arquivo de database para os jogos da steam (200 jogos), ps4/ps5 (100 jogos), xbox (100 jogos) 
    
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
        for id_jogo, info in st_games.items():
            print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
        print("-" * 30)
        print("Caso queira voltar, digite 'EXIT'")

        # Escolha dos jogos que vai adicionar no carrinho
        escolha_jogos = input("Digite o ID do jogo que deseja adicionar no carrinho: ")
        try:
            if escolha_jogos.upper() == "EXIT":
               break
            
            id_jogo = int(escolha_jogos)
            if id_jogo in st_games:                           # Verifica se o ID que a pessoa digitou esta no dicionarios dos jogos
                carrinho_steam[id_jogo] = st_games[id_jogo]         #Adicionando o a lista do jogo completa(ID_jogo, nome, preço) 
                print(f"⏳ Adicionando jogo ao carrinho")
                sleep(3)
                print(f"✅ {st_games[id_jogo]["nome"]} adicionado ao carrinho")

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
                for id_jogo, info in carrinho_steam.items():
                    print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
                    total += info['preco']
                print("=" * 40)
                print(f"💰 Total: R$ {total:>7.2f}")
            
        elif escolha_ver_carrinho_steam == "NAO" or escolha_ver_carrinho_steam == "NÃO" or escolha_ver_carrinho_steam == "N": 
            print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")
            
    except ValueError:
        print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")
def menu_ps4():
    
        #Dicionario do carrinho que vai retornar o valor pra função
    carrinho_ps4 = {}

    # FELIPE -> Criei um arquivo de database para os jogos da steam (200 jogos), ps4/ps5 (100 jogos), xbox (100 jogos) 
    
        #Esse while exibe a parte que mostra os jogos disponiveis, e adiciona no carrinho 
    while True:
        print("""
    ========================================
            Estoque do PS4/PS5
            O que você deseja?
    ========================================
    """)
        
        # Exibe os jogos disponiveis
        print("📦 Estoque de Jogos:")
        print ("=" * 30)
        for id_jogo, info in ps5_games.items():
            print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
        print("-" * 30)
        print("Caso queira voltar, digite 'EXIT'")

        # Escolha dos jogos que vai adicionar no carrinho
        escolha_jogos = input("Digite o ID do jogo que deseja adicionar no carrinho: ")
        try:
            if escolha_jogos.upper() == "EXIT":
               break
            
            id_jogo = int(escolha_jogos)
            if id_jogo in ps5_games:                           # Verifica se o ID que a pessoa digitou esta no dicionarios dos jogos
                carrinho_ps4[id_jogo] = ps5_games[id_jogo]         #Adicionando o a lista do jogo completa(ID_jogo, nome, preço) 
                print(f"⏳ Adicionando jogo ao carrinho")
                sleep(3)
                print(f"✅ {ps5_games[id_jogo]["nome"]} adicionado ao carrinho")

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
                    print("Valor invalido, Retornando ao menu do ps4/ps5")
            else:
                print("❌ Escolha invalida. Digite o numero correspondente ao ID do jogo.")
        except ValueError:
            print("❌ Escolha invalida. Digite o numero correspondente ao ID do jogo.")
    
   ## obs: tirar de dentro dessa função e criar outra pra ver o carrinho da steam
    #ofere a escolha de ver oq ela selecionou no carrinho e volta pro menu de estoque 
    
    escolha_ver_carrinho_ps4 = input("Deseja ver seu carrinho de jogos do ps4/ps5 antes de voltar ?").upper()
    try:
        if escolha_ver_carrinho_ps4 == "SIM" or escolha_ver_carrinho_ps4 == "S":
                print("\n🛒 Seu Carrinho:")
                print("=" * 40)
                total = 0
                for id_jogo, info in carrinho_ps4.items():
                    print(f"{id_jogo:02d}. 🎮 {info['nome']:<30} | R$ {info['preco']:>7.2f}")
                    total += info['preco']
                print("=" * 40)
                print(f"💰 Total: R$ {total:>7.2f}")
                print("voltando para a escolha de plataforma")
                sleep(2)
            
        elif escolha_ver_carrinho_ps4 == "NAO" or escolha_ver_carrinho_ps4 == "NÃO" or escolha_ver_carrinho_ps4 == "N": 
            print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")
            
    except ValueError:
        print("Voltando para a aba de estoque, Caso queira escolher mais jogos de outras plataformas.")



menu_loja_jogo()