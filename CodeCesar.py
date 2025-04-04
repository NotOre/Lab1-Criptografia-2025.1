import argparse

def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += caracter

    return resultado

# Configurar argumentos desde la terminal
parser = argparse.ArgumentParser(description="Cifrado César en Python")
parser.add_argument("texto", type=str, help="Texto a cifrar (entre comillas si tiene espacios)")
parser.add_argument("desplazamiento", type=int, help="Número de desplazamiento")

args = parser.parse_args()

# Mostrar el resultado
texto_cifrado = cifrado_cesar(args.texto, args.desplazamiento)
print(f"Texto cifrado: {texto_cifrado}")
