import socket
from datetime import datetime

# Sello de identidad Zorribandi 🦨🛡️
print("-" * 40)
print("   ZORRI-SCANNER v1.0 🦨🛡️")
print(f"   Iniciado: {datetime.now().strftime('%H:%M:%S')}")
print("-" * 40)

target = input("Introduce la IP o dominio a revisar: ")

def scan_port(ip, port):
    try:
        # Creamos un socket para intentar la conexión
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Puerto {port}: ABIERTO 🛡️")
        sock.close()
    except:
        pass

# Escaneamos puertos básicos de seguridad
puertos = [21, 22, 80, 443, 8080]
print(f"Escaneando {target}...")

for p in puertos:
    scan_port(target, p)

print("\nEscaneo finalizado. 🦨")

