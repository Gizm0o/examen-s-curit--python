import re
from collections import defaultdict, Counter

def parse_log_line(line):
    # Regex pour parser une ligne de journal commun
    log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\S+)')
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    failed_login_attempts = defaultdict(int)
    suspicious_urls = defaultdict(int)
    traffic_by_ip = defaultdict(int)
    status_counter = Counter()

    for line in logs:
        log_data = parse_log_line(line)
        if log_data:
            ip = log_data['ip']
            url = log_data['url']
            status = int(log_data['status'])
            method = log_data['method']
            
            # Incrémenter le compteur de trafic par IP
            traffic_by_ip[ip] += 1

            # Vérifier les tentatives de connexion échouées (ex: status 401 Unauthorized)
            if status == 401:
                failed_login_attempts[ip] += 1
            
            # Identifier les accès à des URL suspectes
            if re.search(r'/admin|/login|/wp-admin|/phpmyadmin', url):
                suspicious_urls[ip] += 1

            # Compter les codes de statut HTTP
            status_counter[status] += 1
    
    # Identifier les IPs avec des tentatives de connexion échouées élevées
    potential_attackers = {ip: count for ip, count in failed_login_attempts.items() if count > 5}

    # Identifier les IPs avec un accès élevé à des URL suspectes
    suspicious_activity = {ip: count for ip, count in suspicious_urls.items() if count > 3}

    # Identifier les IPs avec un trafic anormalement élevé
    high_traffic_ips = {ip: count for ip, count in traffic_by_ip.items() if count > 100}

    return {
        'failed_login_attempts': failed_login_attempts,
        'suspicious_urls': suspicious_urls,
        'status_counter': status_counter,
        'potential_attackers': potential_attackers,
        'suspicious_activity': suspicious_activity,
        'high_traffic_ips': high_traffic_ips,
    }

# Spécifier chemin log server
log_file_path = input("Chemin vers le fichier de log : ")
results = analyze_logs(log_file_path)

print("-> Tentatives de connexion échouées par IP:", results['failed_login_attempts'])
print("-> Activités suspectes par IP (URL suspectes):", results['suspicious_urls'])
print("-> Compteur des statuts HTTP:", results['status_counter'])
print("-> IP avec tentatives de connexion échouées élevées:", results['potential_attackers'])
print("-> IP avec activités suspectes élevées:", results['suspicious_activity'])
print("-> IP avec trafic anormalement élevé:", results['high_traffic_ips'])

