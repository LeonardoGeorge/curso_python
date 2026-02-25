# Criando um dicionário com alguns pares chave-valor
dicionario = {
    "nome": "Leonardo",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando dicionario
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f'nome: {nome}, idade: {idade}, cidade: {cidade}')

# Adicionando um novo chave-valor
dicionario["profissão"] = "tec Banco de dados"
print(f'Dicionario atualizado: {dicionario}')

# Modificando valor
dicionario["idade"] = "25"

# Removendo um par chave-valor
del dicionario["cidade"]
print(f'Dicionario atualizado: {dicionario}')

# Acessando todas as chaves e valores
chaves = dicionario.keys()
valores = dicionario.values()
print(f'Chaves: {chaves}')
print(f'Valores: {valores}')

# Iterando sobre o dicionario
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

# Verificando se existe uma chave no dicionario
if "cidade" in dicionario:
    print(f'Existe a chave cidade: {dicionario["cidade"]}')
else:
    print(f'A chave cidade não existe')

# Usando o metodo get() para acessar valores de forma segura
profissao = dicionario.get("profissão", "Desconhecido")
print(profissao)

# Limpando todos os elementos do dicionario
dicionario.clear()
print(f'Dicionario atualizado: {dicionario}')