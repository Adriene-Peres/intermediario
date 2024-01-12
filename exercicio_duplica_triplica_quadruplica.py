# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def operacao(op):
    if op == 'duplicar':
        def multiplicar(num):
            return num*2
    elif op == 'triplicar':
        def multiplicar(num):
            return num*3
    elif op == 'quadruplicar':
        def multiplicar(num):
            return num*4
    return multiplicar

duplicar_num = operacao('duplicar')
triplicar_num = operacao('triplicar')
quadruplicar_num = operacao('quadruplicar')

for numero in (1,2,3,4,5,6):
    print(duplicar_num(numero), triplicar_num(numero), quadruplicar_num(numero) )
    print('---------------------------')
  

"""
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2)) 
"""