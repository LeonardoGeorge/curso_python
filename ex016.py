lista = [10,20, 30, 40, 50]

# Exibindo primeiros elementos
primeiro_elemento = lista[0]
segundo_elemento = lista[1]
print(primeiro_elemento)
print(segundo_elemento)

# Add elementos
lista.append(60)
print(f'Lista add elemento 60: {lista}')

# Inseriendo elementto em uma posição específica
lista.insert(2,25)
print(f'Lista add elemento 25: {lista}')

# Removendo um elemento da lista
lista.remove(40)
print(f'Lista remove elemento 40: {lista}')

# Removendo ultimo elemento da lista
lista.pop()
print(f'Lista remove último elemento: {lista}')

# Acesando um subgrupo da lista
sub_lista = lista[1:4]
print(f'Sub-lista: {sub_lista}')

# Ordenando a lista
lista.sort()
print(f'Lista sorteada: {lista}')

# Iterando sobre os elementos da lista
print(f'Lista iterada:')
for elemento in lista:
    print(elemento)

