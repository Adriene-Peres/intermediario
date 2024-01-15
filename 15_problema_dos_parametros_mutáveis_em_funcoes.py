# problema dos parÂmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista=[]
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('adriene')
adiciona_clientes('joana', cliente1)
adiciona_clientes('guilherme', cliente1)
cliente1.append("eduardo")


cliente2 = adiciona_clientes('maria')
adiciona_clientes('vitor', cliente2)

cliente3 = adiciona_clientes('joao')
adiciona_clientes('carol', cliente3)


print(cliente1)
print(cliente2)
print(cliente3)