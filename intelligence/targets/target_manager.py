# 🦨🛡️ Gestión de Objetos de Investigación
def add_target(ip):
    with open("targets.txt", "a") as f:
        f.write(f"{ip}\n")
    print(f"[🦨🛡️] Objetivo {ip} añadido a la base de inteligencia.")
