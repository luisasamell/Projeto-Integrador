def numeros_pares(numero):
    return list(filter(lambda x: x % 2 == 0, range(1, numero + 1)))

# Exemplo de uso
numero = 10
print(numeros_pares(numero))  # Saída: [2, 4, 6, 8, 10]

def bombons (dinheiros, preco):
    n_bombons = dinheiro // preco
    troco = dinheiro % preco
    return n_bombons, troco

def a_mais(dinheiro,preco):
    qtd, troco = bombons(dinheiro, preco)
    return preco - troco
