from pedidos import Pedidos

listaProdutos = ['-', 'Hambúrguer', 'X-Burguer', 'Salgado', 'Cachorro-quente', 'Refri Lata', 'Refri 2L', 'Água', 'Chá Gelado']

class Cliente():
    def __init__(self, nome, cpf, endereco, num, final):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.num = num
        self.pedido = Pedidos(num)
        self.final = final
        self.entregue = False
   
    def getInfos(self):
        print("NOME: {}\nCPF: {}\nENDEREÇO: {}\n".format(self.nome, self.cpf, self.endereco))
    
    def getNome(self):
        print("NOME: {}".format(self.nome))
    
    def getCPF(self):
        print("CPF: {}".format(self.cpf))
    
    def getEndereco(self):
        print("ENDEREÇO: {}".format(self.endereco))
    
    def setNome(self, nome):
        self.nome = nome
    
    def setCPF(self, cpf):
        self.cpf = cpf
    
    def setEndereco(self, endereco):
        self.endereco = endereco
    
    def realizarPedido(self, qtd, item, lista):
        for j in range(qtd):
            self.pedido.itens.append(listaProdutos[item])
        for c in range(len(lista)):
           if lista[c].codigo == item:
                self.final+= lista[c].preco * qtd

    def finalizarPedido(self):
        self.entregue = True
        print("O valor final do pedido é de R${:.2f}".format(self.final))
        print("O pedido está saindo para entrega no endereço {}...".format(self.endereco))
        print("O pedido foi entregue!")