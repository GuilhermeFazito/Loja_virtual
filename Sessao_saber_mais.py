from time import sleep


def menu_das_informacoes_da_loja():
    while True:
        print(f"""
=========================================================
           LOJA DE PRODUTOS DIGITAIS!
=========================================================

 - DESCRIÇÃO
     Oferecemos uma variedade de Gifts Cards
     e jogos para as plataformas: Playstation, 
     Xbox, Steam, Google Play, Nitendo e mui-
     to mais. Compre de forma rápida e segura
     e receba seu código por E-mail ou na hora
     direto na sua conta
          
 - BENEFÍCIOS
     ✅ Entrega imediata após a confirmação do pagamento

     ✅ Diversas formas de pagamento (Pix, cartão, boleto)

     ✅ Atendimento humanizado e suporte ágil

     ✅ Preços acessíveis e promoções frequentes

     ✅ 100% seguro e confiável, com proteção antifraude""")
        print(f"""
 - COMO FUNCIONA
     1. Escolha o gift card ou jogo desejado
     2. Adicione ao carrinho e finalize a compra
     3. Receba o código por E-mail ou diretemente na sua 
     conta
     4. Ative o código e aproveite!
        """)
        sleep(0.5)
        voltar = input("Aperte ENTER para voltar: ").upper()
        if voltar == '':
            break
        else:
            print(f"Aperte enter para voltar!")
        

if __name__ == "__main__":
    menu_das_informacoes_da_loja()