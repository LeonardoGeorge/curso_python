print("antes while")
palavra = input("Digite uma palavra: ")
while palavra != "sair":
    print("Dentro while")
    palavra = input("Digite sair para encerrar o laço: ")
print("Você digitou sair e agora está fora do laço")