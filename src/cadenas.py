def invierte_cadena(cadena):
    resultado = ""
    for c in cadena:
        resultado = c + resultado
    return resultado
cadena = "atatap"
assert invierte_cadena(cadena) == "patata"

def es_palindromo(cadena, ignora_espacios:bool = False, ignora_mayúsculas:bool = False):
    if ignora_espacios:
        cadena = cadena.replace(" ", "")
    if ignora_mayúsculas:
        cadena = cadena.lower()
    return invierte_cadena(cadena) == cadena

def estiliza_mensaje(cadena, alterna_may_min:bool = True, usa_dieresis:bool = False, sustituye_espacios:str = " "):
    if alterna_may_min == True:
        resultado =""
        last_upper = False
        for c in cadena:
            if c.isalpha():
                if last_upper == False:
                    c = c.upper()
                last_upper = not last_upper
            resultado += c
    else:
        resultado = cadena
    if usa_dieresis:
        resultado = resultado.replace("a","ä").replace("A","Ä").replace("e","ë").replace("E","Ë").replace("i","ï").replace("I","Ï").replace("o","ö").replace("O","Ö").replace("u","ü").replace("U","Ü")

    resultado = resultado.replace(" ", sustituye_espacios)
    return resultado

