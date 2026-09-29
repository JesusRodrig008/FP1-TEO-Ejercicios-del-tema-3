alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
def letra_a_posicion(letra):
    if letra.isalpha():
        res = alfabeto.find(letra)
        return res
def posicion_a_letra(posicion):
    if posicion.isdigit():
        res = alfabeto[posicion]
        return res

def cifra_cesar(cadena, clave:int):
    res = ""
    for c in cadena:
        s = letra_a_posicion(c)
        s += clave
        if s > len(alfabeto):
            s -= len(alfabeto)
        cha = posicion_a_letra(s)
        res += cha
    return res
cadena = input("Cadena:")
clave = int(input("Clave:"))
print(cifra_cesar(cadena, clave))
print(cadena.find("c"))
