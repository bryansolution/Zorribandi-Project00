import nmap
import json
import os

# Configuración de Zorribandi
TARGET = "192.168.0.1"
DB_FILE = "puertos_conocidos.json"

def scan_network():
    nm = nmap.PortScanner()
    print(f"🦨 Zorribandi buscando cambios en {TARGET}...")
    # Escaneamos los puertos que ya sabemos que son interesantes
    nm.scan(TARGET, '80,443,5000,8081')
    
    found_ports = []
    if TARGET in nm.all_hosts():
        for proto in nm[TARGET].all_protocols():
            lport = nm[TARGET][proto].keys()
            for port in lport:
                if nm[TARGET][proto][port]['state'] == 'open':
                    found_ports.append(port)
    return sorted(found_ports)

def load_previous():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def save_current(ports):
    with open(DB_FILE, 'w') as f:
        json.dump(ports, f)

if __name__ == "__main__":
    try:
        current_ports = scan_network()
        previous_ports = load_previous()

        if not previous_ports:
            print("🛡️ Primera vez: Guardando puertos base en el JSON.")
            save_current(current_ports)
            print(f"Puertos detectados inicialmente: {current_ports}")
        else:
            new_ports = [p for p in current_ports if p not in previous_ports]
            if new_ports:
                print(f"⚠️ ¡ALERTA DE SEGURIDAD! Puertos nuevos detectados: {new_ports} 🦨🛡️")
            else:
                print("✅ Todo en orden. La madriguera sigue segura.")
        
        save_current(current_ports)
    except Exception as e:
        print(f"❌ Error en la vigilancia: {e}")


