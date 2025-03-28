from scapy.all import IP, ICMP, send
import sys

def enviar_icmp(destino, mensaje):
    for caracter in mensaje:
        paquete = IP(dst=destino)/ICMP()/caracter.encode()
        send(paquete, verbose=False)
        print(f"Enviado: {caracter}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: sudo python3 script.py <IP_destino> <mensaje>")
        sys.exit(1)
    
    ip_destino = sys.argv[1]
    mensaje = sys.argv[2]
    
    enviar_icmp(ip_destino, mensaje)
