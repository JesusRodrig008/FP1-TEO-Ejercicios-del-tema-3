alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
def letra_a_posicion(letra):
    if letra.isalpha():
        res = alfabeto.find(letra)
        return res
def posicion_a_letra(posicion):
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

def rompe_clave(texto_codificado):
    for clave in range(len(alfabeto)):
        texto = cifra_cesar(texto_codificado, -clave)
        print(f"(clave {clave}): {texto}")

print(rompe_clave("cfcf"))

