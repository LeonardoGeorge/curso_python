def func1():
    global x
    x = 10
    print(f'função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
print(f'Programa principal - x = {x}')
func1()
print(f'após func1 - x = {x}')
func2()
print(f'após func2 - x = {x}')
