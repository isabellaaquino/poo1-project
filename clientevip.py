from clientes import Cliente

class ClienteVIP(Cliente):
    def __init__(self, nome, cpf, endereco, num, final, desconto):
        Cliente.__init__(self, nome, cpf, endereco, num, final)
        self.desconto = desconto

    def getDesconto(self):
        print("O desconto sobre a compra será de {}%.".format(self.desconto))

    def setDesconto(self, desconto):
        self.desconto = desconto
    
    def finalizarPedido(self):
        desc = 100 - self.desconto
        self.final = self.final * desc/100
        print("O valor final do pedido é de R${:.2f}".format(self.final))
        print("O pedido está saindo para entrega no endereço {}.".format(self.endereco))
        print("O pedido foi entregue!")