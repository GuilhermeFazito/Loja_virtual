from time import sleep

def menu_estoque():
    while True:
        print("""
=========================================
    Bem vindo ao nosso estoque
        Escolha os itens
========================================
              
1) STEAM
2) PS4/PS5
3) XBOX
4) Outros
5) Voltar
 """)
        escolha_estoque = int(input("Digite sua escolha de 1 a 5: "))

        if escolha_estoque == 1:
            estoque_steam()
        sleep(100)






def estoque_steam():
    dicionario_jogos_steam = {
        "Black with: wukong" : 199.00,
        "Elden Ring" : 249.90,
        "Fifa 25" : 299.00,
        "The Last of Us Part II" : 229.90,
        "Cuphead + DLC" : 49.99
        }
    
    print("""
========================================
         Estoque da Steam
        O que você deseja?
========================================
""")
    print("📦 Estoque de Jogos:")
    print ("=" * 30)
    for jogo, preco in dicionario_jogos_steam.items():
        print(f"🎮 {jogo:<40} | R$ {preco:>7.2f}")
    print("-" * 30)
    


menu_estoque()