# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# import sys
# # sys.setrecursionlimit(1004) ---> não é recomendo fazer

# def recursiva(inicio=0, fim=10):
#     # caso base
#     if inicio >= fim:
#         return fim
#     # caso recursivo é contar até chegar no final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0, 100))

# -----------------------------------------------------
# Fatorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print('Fatorial: ')
print(factorial(5))
print(factorial(7))
