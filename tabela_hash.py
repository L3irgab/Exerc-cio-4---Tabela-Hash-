from no_hash import No


class TabelaHash:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tabela = [None] * capacidade
        self.qtde_empregados = 0
        
    def hash(self, id):
        return id % self.capacidade

    def inserir(self, empregado):
        indice = self.hash(empregado.id)

        novo_no = No(empregado)

        novo_no.proximo = self.tabela[indice]
        self.tabela[indice] = novo_no

        self.qtde_empregados += 1

    def buscar(self, id):
        indice = self.hash(id)
        atual = self.tabela[indice]

        while atual is not None:
            if atual.empregado.id == id:
                return atual.empregado
            atual = atual.proximo

        return None

    def remover(self, id):
        indice = self.hash(id)
        atual = self.tabela[indice]
        anterior = None

        while atual is not None:
            if atual.empregado.id == id:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.qtde_empregados -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def imprimir_tabela(self):
        print(f"Tabela Hash - capacidade: {self.capacidade} | empregados: {self.qtde_empregados}")
        print("-----------------------------------------")

        for i in range(self.capacidade):
            print(f"bucket[{i}] -> ", end="")

            if self.tabela[i] is None:
                print("vazio")
            else:
                atual = self.tabela[i]
                while atual is not None:
                    print(f"[{atual.empregado.id} - {atual.empregado.primeiro_nome} {atual.empregado.ultimo_nome}]", end="")
                    if atual.proximo is not None:
                        print(" -> ", end="")
                    atual = atual.proximo
                print()

        print("-----------------------------------------")
