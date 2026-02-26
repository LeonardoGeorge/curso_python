import json
from operator import truediv

from django.utils.text import normalize_newlines

ARQUIVO = 'contas.json'

def carregar_contas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except:
        return {}

def salvar_contas(contas):
    with open(ARQUIVO, 'w') as f:
        json.dump(contas, f, indent=4)

def criar_conta(nome, senha):
    contas = carregar_contas()

    for conta in contas:
        if conta['nome'] == nome:
            return false

    nova_conta = {
        'nome': nome,
        'senha': senha,
        'saldo': 0
    }

    contas.append(nova_conta)
    salvar_contas(contas)
    return True

def login(nome, senha):
    contas = carregar_contas()

    for conta in contas:
        if conta['nome'] == nome and conta['senha'] == senha:
            return conta
    return None

def depositar(conta, valor):
    contas = carregar_contas()

    for c in contas:
        if c["nome"] == conta['nome']:
            c['saldo'] += valor

        salvar_contas(contas)

def sacar(conta, valor):
    contas = carregar_contas()

    for c in contas:
        if c["nome"] == conta['nome']:
            if c['saldo'] >= valor:
                c['saldo'] -= valor
                salvar_contas(contas)
                return True
            else:
                return False

