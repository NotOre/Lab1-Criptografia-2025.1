from scapy.all import sniff, ICMP
import string
import signal
import sys

# Para colorear el texto
GREEN = '\033[92m'
RESET = '\033[0m'

# Lista de palabras comunes en español (puedes agregar más palabras aquí)
PALABRAS_COMUNES = {"informatica", "hola", "mundo", "mensaje", "esto", "es", "una", "prueba", "programa", "computadora",
    "código", "usuario", "sistema", "red", "internet", "técnico", "computación", "conexión", "conocimiento",
    "función", "variable", "algoritmo", "proceso", "tecnología", "análisis", "escritura", "documento", 
    "fácil", "difícil", "rápido", "lento", "computadora", "información", "trabajo", "educación", "ciencia", 
    "estudio", "aprendizaje", "desarrollo", "programación", "móvil", "teclado", "pantalla", "ratón", 
    "base", "dato", "respuesta", "solución", "tarea", "aprendido", "proyecto", "problema", "éxito", 
    "técnica", "práctica", "ejemplo", "teoría", "actividad", "ejercicio", "recursos", "solicitar", 
    "revisar", "conocer", "investigar", "avanzar", "trabajando", "empezar", "terminar", "mejor", "estudio", 
    "conclusión", "aplicación", "experiencia", "habilidad", "avance", "futuro", "crecer", "lograr", "resultados",
    "vacío", "esperar", "seguir", "enviar", "recibir", "conectar", "establecer", "resultados", "éxito", "fracaso"}

caracteres_recibidos = []

def capturar_paquetes(pkt):
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:  # ICMP Echo Request
        carga = bytes(pkt[ICMP].payload)
        if carga:
            try:
                letra = carga.decode('utf-8')[0]
                caracteres_recibidos.append(letra)
                print(f"[+] Recibido carácter: {letra}")
            except Exception:
                pass  # Ignora datos no UTF-8

def cesar_descifrar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - base - desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

def es_mensaje_probable(texto):
    # Evaluamos cuántas palabras comunes contiene el texto descifrado
    palabras = texto.split()
    palabras_validas = sum(1 for palabra in palabras if palabra.lower() in PALABRAS_COMUNES)
    
    # Aumentamos el puntaje si contiene palabras comunes
    return palabras_validas

def mostrar_resultados(mensaje_cifrado):
    print("\n=== Posibles mensajes descifrados (fuerza bruta César) ===")
    puntajes = []

    for shift in range(26):
        descifrado = cesar_descifrar(mensaje_cifrado, shift)
        score = es_mensaje_probable(descifrado)
        puntajes.append((shift, descifrado, score))

    # Encontrar el shift con el puntaje más alto (más probable)
    mejor = max(puntajes, key=lambda x: x[2])

    for shift, texto, score in puntajes:
        if texto == mejor[1]:
            # Resalta en verde la opción con el puntaje más alto (más probable)
            print(f"{GREEN}[{shift}] {texto}{RESET}")
        else:
            print(f"[{shift}] {texto}")

def manejar_ctrl_c(sig, frame):
    print("\n\n🛑 Captura interrumpida por el usuario.")
    mensaje_cifrado = ''.join(caracteres_recibidos)
    print(f"\nMensaje capturado (cifrado): {mensaje_cifrado}")
    mostrar_resultados(mensaje_cifrado)
    sys.exit(0)

if __name__ == "__main__":
    print("Escuchando paquetes ICMP... (Presiona Ctrl+C para detener)")
    signal.signal(signal.SIGINT, manejar_ctrl_c)
    sniff(filter="icmp", prn=capturar_paquetes, store=0)
