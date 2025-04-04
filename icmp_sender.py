from scapy.all import IP, ICMP, send
import time
import argparse

def enviar_icmp_string(destino, mensaje, delay=0.1):
    for i, caracter in enumerate(mensaje):
        paquete = IP(dst=destino)/ICMP()/caracter
        print(f"[{i+1}] Enviando '{caracter}' a {destino}...")
        send(paquete, verbose=False)
        time.sleep(delay)  # Pequeña pausa entre paquetes

    print("✅ Mensaje enviado en paquetes ICMP.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enviar mensaje por ICMP (1 carácter por paquete)")
    parser.add_argument("destino", type=str, help="IP o dominio del receptor")
    parser.add_argument("mensaje", type=str, help="Mensaje a enviar por ICMP")
    parser.add_argument("--delay", type=float, default=0.1, help="Retraso entre paquetes (segundos)")

    args = parser.parse_args()

    enviar_icmp_string(args.destino, args.mensaje, args.delay)
