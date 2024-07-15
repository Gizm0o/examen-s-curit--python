import psutil
import time

def bytes_to_human(n):
    """
    Convertir des octets en un format lisible par l'homme.
    """
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    step_unit = 1024.0
    for symbol in symbols:
        if n < step_unit:
            return f"{n:.2f} {symbol}"
        n /= step_unit
    return f"{n:.2f} Y"

def monitor_network(interface, interval=1):
    """
    Surveiller le trafic réseau sur une interface réseau spécifiée.

    :param interface: L'interface réseau à surveiller.
    :param interval: L'intervalle en secondes pour mettre à jour les statistiques réseau.
    """
    try:
        # Obtenir les statistiques réseau initiales
        initial_stats = psutil.net_io_counters(pernic=True)[interface]
    except KeyError:
        print(f"Erreur : Aucune interface réseau nommée '{interface}'")
        return

    print(f"Surveillance du trafic réseau sur l'interface : {interface}")
    print(f"{'Heure':<8} {'Envoyé':>15} {'Reçu':>15}")

    while True:
        time.sleep(interval)

        try:
            # Obtenir les statistiques réseau actuelles
            current_stats = psutil.net_io_counters(pernic=True)[interface]
        except KeyError:
            print(f"Erreur : Aucune interface réseau nommée '{interface}'")
            return

        # Calculer les octets envoyés et reçus dans l'intervalle
        sent_bytes = current_stats.bytes_sent - initial_stats.bytes_sent
        recv_bytes = current_stats.bytes_recv - initial_stats.bytes_recv

        # Mettre à jour les statistiques initiales pour le prochain intervalle
        initial_stats = current_stats

        # Convertir les octets en format lisible par l'homme
        sent_human = bytes_to_human(sent_bytes)
        recv_human = bytes_to_human(recv_bytes)

        # Afficher les résultats
        print(f"{time.strftime('%H:%M:%S')} {sent_human:>15} {recv_human:>15}")

if __name__ == "__main__":
    # Remplacez 'eth0' par le nom de l'interface réseau que vous souhaitez surveiller
    interface_name = 'eth0'

    # Surveiller le trafic réseau
    monitor_network(interface_name, interval=1)

