# Tabela Hash com Encadeamento (Separate Chaining)

Atividade da disciplina de Estruturas de Dados - 3º Semestre Sistemas de Informação

---

## O que é

Implementação de uma Tabela Hash usando a técnica de **Separate Chaining** para tratar colisões.

Quando dois elementos geram o mesmo índice na tabela, eles ficam guardados numa lista encadeada naquele bucket.

---

## Como funciona

**Função de hash usada:** `indice = id % capacidade`

Com capacidade 5, os empregados ficam assim:

```
1123 % 5 = 3  ->  bucket[3]   Gabriel Brasil
5432 % 5 = 2  ->  bucket[2]   Lucas Souza
2221 % 5 = 1  ->  bucket[1]   Dina Borges
4314 % 5 = 4  ->  bucket[4]   Moises Cerqueira
9993 % 5 = 3  ->  bucket[3]   Ana Lima     (colisao com Gabriel)
7771 % 5 = 1  ->  bucket[1]   Carlos Matos (colisao com Dina)
```

Resultado na tabela depois das colisoes:

```
bucket[0] -> vazio
bucket[1] -> [7771 - Carlos Matos] -> [2221 - Dina Borges]
bucket[2] -> [5432 - Lucas Souza]
bucket[3] -> [9993 - Ana Lima] -> [1123 - Gabriel Brasil]
bucket[4] -> [4314 - Moises Cerqueira]
```

Quando tem colisão, o novo nó entra no início da lista encadeada do bucket.

---

## Arquivos

```
main.py          -> executa o exemplo
tabela_hash.py   -> classe TabelaHash com inserir, buscar, remover e imprimir
no_hash.py       -> no da lista encadeada usada em cada bucket
empregado.py     -> classe Empregado (entidade usada nos exemplos)
```

---

## Como rodar

```bash
python3 main.py
```

Não precisa instalar nada, só Python 3.

---

## Operações implementadas

- `inserir(empregado)` — calcula o bucket e insere no inicio da cadeia
- `buscar(id)` — percorre a lista do bucket até achar o id
- `remover(id)` — remove o nó ajustando os ponteiros
- `imprimir_tabela()` — mostra o estado de todos os buckets
