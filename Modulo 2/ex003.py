# função recursiva contagem regressiva
def regressiva(x):
    print(x)
    if x > 0:
        regressiva(x - 1)
    else:
        print('acabou')

regressiva(10)

# Não recursiva
for i in range(10, -1, -1):
    print(i)
print('acabou')