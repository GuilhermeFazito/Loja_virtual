from listas import Produtos


def compra():
    compra = input("escreva: ")


    if compra in Produtos:
        print("tem esse item")
    else:
        print("")
