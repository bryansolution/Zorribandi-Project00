import socket

def zorri_scan(target):
    print(f"🦨 Zorribandi está olfateando puertos en: {target}")
    # Probaremos los puertos más comunes: 80 (web), 443 (https), 22 (ssh)
    puertos = [22, 80, 443, 8080]
    
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Esperar 1 segundo
        resultado = sock.connect_ex((target, puerto))
        
        if resultado == 0:
            print(f"✅ Puerto {puerto}: ABIERTO")
        else:
            print(f"❌ Puerto {puerto}: CERRADO")
        sock.close()

if __name__ == "__main__":
    objetivo = "google.com" # Puedes cambiarlo por una IP o dominio
    zorri_scan(objetivo)
