# Description

Ce script Python utilise la bibliothèque psutil pour surveiller les tentatives de connexion réseau sur une machine locale.
Le script détecte les connexions entrantes et sortantes et peut signaler celles qui sont suspectes, par exemple, en fonction de critères comme des connexions répétées sur une courte période ou des connexions provenant d'adresses IP non autorisées.

# Prérequis

Avant d'exécuter le script, assurez-vous d'installer la bibliothèque psutil si elle n'est pas déjà installée :

pip install psutil

# Utilisation 

python3 intrusions.py

# Fonctions

### get_active_connections(): 
	Obtient les connexions réseau actives.
### check_for_suspicious_connections(): 
	Vérifie les connexions réseau et détecte les tentatives suspectes basées sur les adresses IP.
### reset_connection_attempts(): 
	Réinitialise le compteur de tentatives de connexion pour chaque adresse IP.
### main() 
	exécute une boucle infinie pour surveiller les connexions réseau à intervalles réguliers (CHECK_INTERVAL)
