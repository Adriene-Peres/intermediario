# Função decoradoras

# def criar_funcao(func):                   # função decoradora
#     def interna(*args, **kwargs):
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         return resultado
#     return interna

# def inverter_string(string):
#     return string[::-1]


# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('"param" deve ser uma string')


# inverter_string_checando_parametro = criar_funcao(inverter_string)
# invertida = inverter_string_checando_parametro('123')
# print(invertida)

# --------------------------------------------------------------

# SYNTAX SUGGAR

# def criar_funcao(func):                   # função decoradora
#     def interna(*args, **kwargs):
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         return resultado
#     return interna

# @criar_funcao   # syntax suggar
# def inverter_string(string):
#     return string[::-1]


# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('"param" deve ser uma string')


# invertida = inverter_string('123')
# print(invertida)

# ----------------------------------------------------------------------

# DECORADORES COM PARÂMETROS
# def fabrica_de_decoradores(a=None,b=None,c=None):
#     def fabrica_de_funcoes(func):
#         print('decoradora 1')

#         def aninhada(*args, **kwargs):
#             print('Aninhada')
#             res = func(*args,**kwargs)
#             return res
#         return aninhada
#     return fabrica_de_funcoes


# @fabrica_de_decoradores(1,2,3)
# def soma(x,y):
#     return x + y

# multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

# dez_mais_cinco = soma(10,5)
# dez_vezes_cinco = multiplica(10,5)
# print(dez_mais_cinco)
# print(dez_vezes_cinco)

# ----------------------------------------------------------------------

# ORDEM DOS DECORADORES

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args,**kwargs):
            res = func(*args,**kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome = 'quinto')
@parametros_decorador(nome = 'quarto')
@parametros_decorador(nome = 'terceiro')
@parametros_decorador(nome = 'segundo')
@parametros_decorador(nome = 'primeiro')
def soma(x,y):
    return x+y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)

