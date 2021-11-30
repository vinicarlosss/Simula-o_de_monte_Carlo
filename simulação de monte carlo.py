import random

def f(x):
    return 5*x + 1


def g(x):
    return 3*x + 1
    return


def monteCarlo(quantidaNumeros,areaRetangulo,a,b):
    pontosDentro = 0
    pontosFora = 0
    for i in range(quantidaNumeros):
        xi = random.uniform(0, m)
        yi = random.uniform(0, n)
        if xi >= a and xi <= b:
            if yi >= g(xi) and yi <= f(xi):
                pontosDentro += 1
            else:
                pontosFora += 1
        else:
            pontosFora += 1

    areaRio = (pontosDentro / (pontosDentro + pontosFora)) * areaRetangulo
    return areaRio



m = float(input("digite o valor que limita o eixo x: "))
n = float(input("digite o valor que limita o eixo y: "))
areaRetangulo = m * n
a = float(input("digite o valor no eixo x para limitar o rio: "))
b = float(input("digite o outro valor no eixo x para limitar o rio: "))

print(monteCarlo(1000,areaRetangulo,a,b))
print(monteCarlo(2000,areaRetangulo,a,b))
print(monteCarlo(3000,areaRetangulo,a,b))
print(monteCarlo(4000,areaRetangulo,a,b))
print(monteCarlo(5000,areaRetangulo,a,b))
print(monteCarlo(10000,areaRetangulo,a,b))
print(monteCarlo(100000,areaRetangulo,a,b))
print(monteCarlo(1000000,areaRetangulo,a,b))
print(monteCarlo(10000000,areaRetangulo,a,b))
print(monteCarlo(100000000,areaRetangulo,a,b))
