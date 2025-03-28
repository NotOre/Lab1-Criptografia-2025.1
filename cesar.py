import sys

def cifrar_cesar(texto: str, desplazamiento: int) -> str:
    resultado = ""
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            nueva_letra = chr(((ord(caracter) - ord('a') + desplazamiento) % 26) + ord('a'))
            resultado += nueva_letra
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 script.py <texto> <desplazamiento>")
        sys.exit(1)
    
    texto_a_cifrar = sys.argv[1]
    desplazamiento = int(sys.argv[2])
    
    texto_cifrado = cifrar_cesar(texto_a_cifrar, desplazamiento)
    print("Texto cifrado:", texto_cifrado)
