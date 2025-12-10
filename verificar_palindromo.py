def verificar_palindromo(palabra):
    palabra = palabra.lower()
    reverso = palabra[::-1]
    
    if palabra == reverso:
        return True
    else:
        return False

entrada = input("Ingrese una palabra: ")
es_palindromo = verificar_palindromo(entrada)

if es_palindromo:
    print(f"La palabra '{entrada}' es un palíndromo.")
else:
    print(f"La palabra '{entrada}' no es un palíndromo.")