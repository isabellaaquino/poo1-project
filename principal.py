from clientes import Cliente
from clientevip import ClienteVIP
from pedidos import Pedidos
from produtos import Produtos   

# Criação de instâncias de Produtos:
Hamburguer = Produtos(1,9.50, '15.12', 400)
XBurguer = Produtos(2,10, '15.12', 500)
Salgado = Produtos(3,5,'10.12',150)
CachorroQuente = Produtos(4,8,'15.12',350)
Refri_Lata = Produtos(5,4.50,'30.02',350)
Refri_2l = Produtos(6,8,'30.02',2000)
Agua = Produtos(7,3,'-',500)
Cha_Gelado = Produtos(8,5, '30.02',350)

# Criação de lista de Produtos:
listaItens = [Hamburguer, XBurguer, Salgado, CachorroQuente, Refri_Lata, Refri_2l, Agua, Cha_Gelado]

# Criação da lista de clientes:
listaClientes = []

#Criação de um dicionário de clientes:
pessoas = {}

# Lista de opções do menu:
opc = [1,2,3,4,5,6]

# 0. Parar o programa
# 1. Registrar um novo cliente
# 2. Registrar um novo cliente VIP
# 3. Começar um novo pedido
# 4. Finalizar seu pedido
# 5. Remover/editar um cliente existente
# 6. Checar informações

print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
menu = int(input("Escolha uma das opções!"))

while menu in opc:
    
    if menu not in opc:
        break

    elif menu == 1:
        pessoas['nome'] = str(input("Digite seu nome."))
        pessoas['cpf'] = str(input("Digite seu cpf."))
        pessoas['endereco'] = str(input("Digite seu endereço."))
        num = len(listaClientes) + 1
        cliente1 = Cliente(pessoas['nome'], pessoas['cpf'], pessoas['endereco'], num, 0)
        listaClientes.append(cliente1)
    
        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))
        
    elif menu == 2:
        nome = input("Digite seu nome.")
        cpf = input("Digite seu cpf.")
        endereco = input("Digite seu endereço.")
        desconto = int(input("Digite o desconto desejado em %."))
        num = len(listaClientes) + 1
        clientevip1 = ClienteVIP(nome, cpf, endereco, num, 0, desconto)
        listaClientes.append(clientevip1)
        
        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))
        
    elif menu == 3:
        
        print("Começando um novo pedido...")
        print("-=-=-    MENU:   -=-=-")
        print("COMIDAS:\n1. Hambúrguer $9.50\n2. X-Burguer $10.00\n3. Salgado(un) $5.00\n4. Cachorro-quente $8.00")
        print("BEBIDAS:\n5. Refrigerante lata $4.50\n6. Refrigerante 2L $8.00\n7. Água mineral $3.00\n8. Chá gelado $5.00")
        
        numero = input("Digite o número de cpf da sua conta")
        quem = '-'
        
        for c in range(len(listaClientes)):
            if listaClientes[c].cpf == numero:
                quem = listaClientes[c]
                break
        
        if quem.entregue == True:
            print("Seu pedido já foi entregue!")
        
        else:
            continuar = int(input("Para adicionar um item digite 1. Para terminar, digite 0."))
            while continuar == 1:
                if continuar == 0:
                    break
                qtd, item = input("Digite a quantidade e o código do item desejado, separado por espaços.").split()
                qtd = int(qtd)
                item = int(item)
                
                quem.realizarPedido(qtd,item,listaItens)
                
                continuar = int(input("Para adicionar um item digite 1. Para terminar, digite 0."))
            
        
        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))    

    elif menu == 4:
        
        numero = input("Digite o número de cpf da sua conta")
        quem = '-'
        for c in range(len(listaClientes)):
            if listaClientes[c].cpf == numero:
                quem = listaClientes[c]
                break
        
        if quem.entregue == True:
            print("Seu pedido já foi entregue!")
        else:
            quem.pedido.getNumero()
            quem.finalizarPedido()

        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))

    elif menu == 5:
        
        quem = input("Digite o cpf do cliente que você irá realizar a mudança/exclusão.")

        escolha = input("Você deseja realizar uma modificação ou uma exclusão? Digite 'M' para modificação ou 'E' para exclusão.").upper()
        while escolha !="M" and escolha!="E":
            print("A entrada não foi correta.")
            escolha = input("Você deseja realizar uma modificação ou uma exclusão? Digite 'M' para modificação ou 'E' para exclusão.").upper()
        
        if escolha == 'M':
            tipo = input("A modificação é de um cliente normal ou um cliente VIP? Digite 'N' para normal, e 'V' para VIP.").upper()
            if tipo == 'N':
                for c in range(len(listaClientes)):
                    if listaClientes[c].cpf == quem:
                        listaClientes.pop(c)
                        nome = input("Digite o novo nome do cliente.")
                        cpf = input("Digite o cpf do cliente.")
                        endereco = input("Digite o endereço do cliente.")
                        num = len(listaClientes) + 1
                        cliente1 = Cliente(nome, cpf, endereco, num, 0)
                        listaClientes.append(cliente1)
            
            elif tipo == 'V':
                for c in range(len(listaClientes)):
                    if listaClientes[c].cpf == quem:
                        listaClientes.pop(c)
                        nome = input("Digite o novo nome do cliente.")
                        cpf = input("Digite o cpf do cliente.")
                        endereco = input("Digite o endereço do cliente.")
                        desconto = int(input("Digite o novo desconto."))
                        num = len(listaClientes) + 1

                        clientevip1 = ClienteVIP(nome, cpf, endereco, num, 0,  desconto)
                        listaClientes.append(clientevip1)
            else:
                print("Você deve digitar 'N' ou 'V' para tipo de cliente.")
                tipo = input("A modificação é de um cliente normal ou um cliente VIP? Digite 'N' para normal, e 'V' para VIP.").upper()
        
        elif escolha == 'E':
            for c in range(len(listaClientes)):
                if listaClientes[c].cpf == quem:
                    listaClientes.pop(c)
        else:
            print("A entrada deve ser 'M' ou 'E'. Digite novamente.")
            escolha = input("Você deseja realizar uma modificação ou uma exclusão? Digite 'M' para modificação ou 'E' para exclusão.").upper()

        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))

    elif menu == 6:
        
        quem = input("Digite o cpf do cliente que você quer checar as informações")
        for c in range(len(listaClientes)):
            if listaClientes[c].cpf == quem:
                quem = listaClientes[c]
                break
        quem.getInfos()
        
        print("0. Parar o programa\n1. Registrar um novo cliente\n2. Registrar um novo cliente VIP\n3. Começar um novo pedido\n4. Finalizar Pedido\n5. Remover/editar um cliente já existente.\n6. Checagem de informações")
        menu = int(input("Escolha uma das opções!"))