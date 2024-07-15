# Description

Ce script en Python utilise la bibliothèque psutil pour surveiller le trafic réseau sur une interface réseau spécifiée. Il affiche la quantité de données envoyées et reçues en un format lisible par l'homme à des intervalles réguliers.

# Installation

Avant d'exécuter le script, assurez-vous d'installer la bibliothèque psutil si elle n'est pas déjà installée. Vous pouvez l'installer en utilisant pip :

```
pip install psutil
```

# Utilisation :

```
python3 surveillance_reseau.py
```

Entrez ensuite l'interface réseau que vous voulez surveillez et ensuite l'intervalle entre chaque analyse du réseau de l'interface entrée

# Fonctions :

### bytes_to_human(n)

Cette fonction convertit un nombre d'octets en un format plus lisible par l'homme (par exemple, Ko, Mo, Go).

- Paramètre :
    n : Le nombre d'octets à convertir.

- Retourne :
    Une chaîne de caractères représentant la valeur convertie en unités lisibles par l'homme.

### monitor_network(interface, interval=)

Cette fonction surveille le trafic réseau sur une interface spécifiée et affiche les octets envoyés et reçus à des intervalles réguliers.

- Paramètres :
        interface : Le nom de l'interface réseau à surveiller.
        interval : L'intervalle en secondes entre chaque mise à jour des statistiques (par défaut 1 seconde).

- Fonctionnement :
        Obtient les statistiques réseau initiales pour l'interface spécifiée.
        Affiche un en-tête avec les colonnes "Heure", "Envoyé" et "Reçu".
        Dans une boucle infinie, attend l'intervalle spécifié, puis obtient les statistiques réseau actuelles et calcule la différence avec les statistiques initiales pour déterminer les octets envoyés et reçus pendant cet intervalle.
        Affiche les résultats sous un format lisible par l'homme.

