from cadenas import invierte_cadena
def invierte_numero(numero):
    res = 0
    while numero != 0:
        n = numero % 10
        res *=10
        res+=n
        numero //=10

    return res


def convierte_binario(numero):
    res = ""
    while numero != 0:
        n = str(numero % 2)
        res += n
        numero //=2
    res = invierte_cadena(res)
    if res == "":
        res += "0" 
    return res

def sumar_divisores_propios(numero):
    res = 0
    for i in range(1,numero):
        if numero % i == 0:
            res += i
    return res

def clasifica_numero(numero):
    if sumar_divisores_propios(numero) == numero:
        return "Perfecto"
    elif sumar_divisores_propios(numero) < numero:
        return "Abundante"
    else:
        return "Deficiente"

def busca_perfecto(n):
    i = 0
    num = 1
    while i < n:
        num += 1
        if clasifica_numero(num) == "Perfecto":
            i += 1
    return num
def clasifica_rango(numero):
    for i in range (numero):
        print(clasifica_numero(i))


print(busca_perfecto(1))
