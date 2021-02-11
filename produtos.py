class Produtos():
    def __init__(self, codigo, preco, validade, peso):
        self.codigo = codigo
        self.preco = float(preco)
        self.validade = validade
        self.peso = peso

    def getProduto(self):
        print("O preço do produto é {}, de validade {} e peso {}g.".format(self.preco, self.validade, self.peso))

    def setProduto(self, preco, validade, peso):
        self.preco = int(preco)
        self.validade = validade
        self.peso = peso