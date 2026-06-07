class Empregado:

    def __init__(self, id, primeiro_nome, ultimo_nome):
        self.id = id
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

    def __str__(self):
        return f"Empregado{{ id={self.id}, primeiroNome='{self.primeiro_nome}', ultimoNome='{self.ultimo_nome}' }}"
