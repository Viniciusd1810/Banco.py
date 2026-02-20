class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    @property
    def endereco_formatado(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado}"

    def __str__(self):
        return self.endereco_formatado
