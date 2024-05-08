def questao1 (nome, idade, cidade):
    print("Nome", nome, sep=' : ', end=' - ')
    print("Idade", idade, sep=' : ', end=' - ')
    print("Cidade", cidade, sep=' : ', end='!\n')

# Exemplo de uso:
questao1("Luisa", "21", "Rio de Janeiro!")

def questao2():
    nl_texto = input('Entre com o primeiro número: ')
    nl = float(nl_texto)

    n2 = float(input('Entre com o segundo número: '))

    op = input('Entre com a operação: ')

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '*':
        print (n1 * n2)
    else:
        print('Operador desconhecido')
        
# Exemplo de uso:
questao2()

def questao3():
    texto = input ("Entre com os itens da lista de compras separados por vírgula:")


    lista = texto.split(',')

    contador = 1
    for item in lista:
        print("Item", contador, ": ", item, sep='')
        contador +=1

# Exemplo de uso:
questao3()
        
def questao4():
    celsius = float(input('Entre a temperatura em Celsius:'))
    fahreneit = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é:", fahreneit)

# Exemplo de uso:
questao4()

def questao5():
    nomes = []

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nomes.append(nome)

    print("\nNomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso:
questao5()
