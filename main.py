from empregado import Empregado
from tabela_hash import TabelaHash


def main():
    tabela = TabelaHash(5)

    empregado1 = Empregado(1123, "Gabriel", "Brasil")    
    empregado2 = Empregado(5432, "Lucas",   "Souza")     
    empregado3 = Empregado(2221, "Dina",    "Borges")    
    empregado4 = Empregado(4314, "Moises",  "Cerqueira") 

    tabela.inserir(empregado1)
    tabela.inserir(empregado2)
    tabela.inserir(empregado3)
    tabela.inserir(empregado4)

    print("1.-----------------------")
    tabela.imprimir_tabela()

    empregado5 = Empregado(9993, "Ana",    "Lima")
    empregado6 = Empregado(7771, "Carlos", "Matos")

    tabela.inserir(empregado5)
    tabela.inserir(empregado6)

    print("2.-----------------------")
    tabela.imprimir_tabela()

    print("3.-----------------------")
    encontrado = tabela.buscar(9993)
    print(encontrado)

    print("4.-----------------------")
    tabela.remover(1123)
    tabela.imprimir_tabela()


main()
