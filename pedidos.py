class Pedidos():
    def __init__(self, numero):
        self.numero = numero
        self.itens = []
        
    def getNumero(self):
        print("O número do seu pedido é {}.".format(self.numero))
        print("O seu pedido tem os seguintes itens:")
        for j in self.itens:
            print("-", j)
    
    def setNumero(self, numero):
        self.numero = numero

    def removerItem(self, item):
        self.itens.pop(item)
    
    def adicionarItem(self, item):
        self.itens.append(item)