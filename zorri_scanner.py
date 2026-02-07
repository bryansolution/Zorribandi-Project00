# 🦨🛡️ ZORRIBANDI - ELITE SECURITY SCANNER (ULTRA-HARDENED)
# Uso exclusivo para investigación de seguridad ética.

import os
import sys
import subprocess

def imprimir_firma():
    print("""
    [ 🦨🛡️ ZORRIBANDI SECURITY RESEARCHER ]
    [ PROTOCOLO: RECONOCIMIENTO MASIVO     ]
    """)

def check_dependencies():
    # 🦨🛡️ Verificando que el laboratorio tenga las herramientas necesarias
    tools = ["nmap", "python"]
    for tool in tools:
        if subprocess.run(["which", tool], capture_output=True).returncode != 0:
            print(f"🚨 ERROR: Falta la herramienta '{tool}'. Instálala primero.")
            sys.exit(1)

def ultra_scanner():
    imprimir_firma()
    target = input("💠 [🦨🛡️] Introduce el objetivo (IP/Dominio): ")
    
    print(f"\n[!] Iniciando Escaneo de Seguridad Masiva en: {target}")
    
    # EXPLICACIÓN DE LA SEGURIDAD MASIVA APLICADA:
    # -sS: TCP SYN Scan (Sigiloso, no completa la conexión)
    # -Pn: No hace ping (Evita ser detectado por firewalls que bloquean ICMP)
    # -T2: Tiempo lento (Para evitar sistemas de detección de intrusos)
    # --script vuln: Ejecuta la base de datos de vulnerabilidades conocida
    
    comando = [
        "nmap", "-sS", "-Pn", "-T2", 
        "--script", "vuln", 
        "-oN", f"auditoria_{target}.🦨🛡️.txt", 
        target
    ]
    
    try:
        print("🕵️  Olfateando vulnerabilidades en modo sigilo... (Esto puede tardar)")
        subprocess.run(comando)
        print(f"\n✅ [🦨🛡️] Informe generado: auditoria_{target}.🦨🛡️.txt")
    except Exception as e:
        print(f"🚨 Error en el escáner: {e}")

if __name__ == "__main__":
    check_dependencies()
    ultra_scanner()
