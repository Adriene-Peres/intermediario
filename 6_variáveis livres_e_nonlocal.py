# variáveis livres + nonlocal 

# locals = função que retorna as variavéies locais 
# globals = função que retorna as variáveis globais 
# variavéis livres que são nonlocal podem ser alteradas dentro do escopo de uma função

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_cocatenar=''):
        nonlocal valor_final
        valor_final += valor_a_cocatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()
print(final)




