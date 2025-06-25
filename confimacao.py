import menu

def confirmacao():
    print("""
        Você deseja realizar a compra agora? 
    1) Sim
    2) Não
    """)
    escolha_confirmacao = input("Digise sua escolha: ")
    if escolha_confirmacao == 1:
        print("Carregando para a pagina de compra")
    elif escolha_confirmacao == 2:
        print("voltando pra tela de menu")
        menu()
    
   