# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *=  numero
    return (total)

m1 = multiplicar(1,2,3,4)
m2 = multiplicar(1,1,1,2,2,2)
print(m1)
print(m2)


print('---------------------------------------------------')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero%2 == 0:
        return f"{numero} é par"
    return f"{numero} é impar"

aux = par_impar(3)
print(aux)
print(par_impar(8))

