import psutil
import time
from collections import defaultdict

# détection
ALLOWED_IPS = ['192.168.99.1', '192.168.99.100']  # range d'adresses IP locales (exemple)
SUSPICIOUS_THRESHOLD = 3  # nombre de connexions suspectes avant de déclencher une alerte
CHECK_INTERVAL = 5  # récurence des vérifications en secondes

# Dictionnaire pour suivre les tentatives de connexion par IP
connection_attempts = defaultdict(int)

def get_active_connections():
    """Obtient les connexions réseau actives"""
    return psutil.net_connections(kind='inet')

def check_for_suspicious_connections():
    """Vérifie les connexions réseau pour détecter les tentatives suspectes"""
    active_connections = get_active_connections()
    for conn in active_connections:
        if conn.raddr:
            remote_ip = conn.raddr.ip
            # Ignorer les connexions provenant des IPs autorisées
            if remote_ip not in ALLOWED_IPS:
                connection_attempts[remote_ip] += 1
                if connection_attempts[remote_ip] > SUSPICIOUS_THRESHOLD:
                    print(f"ALERTE : Tentative de connexion suspecte détectée de l'adresse IP {remote_ip}")

def reset_connection_attempts():
    """reset le compteur de tentatives de connexion"""
    connection_attempts.clear()

def main():
    """surveiller les connexions"""
    while True:
        check_for_suspicious_connections()
        time.sleep(CHECK_INTERVAL)
        reset_connection_attempts()

if __name__ == "__main__":
    main()
