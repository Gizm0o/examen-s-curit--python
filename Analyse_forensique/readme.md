# Description

Ce script en Python analyse les fichiers de log d'un serveur web pour identifier diverses activités, telles que les tentatives de connexion échouées, les accès à des URLs suspectes, et le trafic anormalement élevé par IP.

## Installation

Ce script utilise uniquement les bibliothèques standard de Python, il n'y a donc pas de dépendances supplémentaires à installer.

## Utilisation

```
python3 analyze_log.py
```

Entrez ensuite le chemin vers le fichier de log que vous souhaitez analyser lorsque cela vous est demandé.

## Fonctions

### parse_log_line(line)

Cette fonction analyse une ligne de log en utilisant une expression régulière pour extraire des informations clés.

- Paramètre :
  - `line` : Une ligne du fichier de log à analyser.

- Retourne :
  Un dictionnaire contenant l'IP, le timestamp, la méthode HTTP, l'URL, le code de statut, et la taille de la réponse.

### analyze_logs(file_path)

Cette fonction analyse le fichier de log spécifié et retourne un résumé des activités.

- Paramètre :
  - `file_path` : Le chemin vers le fichier de log à analyser.

- Retourne :
  Un dictionnaire avec les informations suivantes :
  - `failed_login_attempts` : Tentatives de connexion échouées par IP.
  - `suspicious_urls` : Activités suspectes par IP (accès à des URLs suspectes).
  - `status_counter` : Compteur des statuts HTTP.
  - `potential_attackers` : IP avec des tentatives de connexion échouées élevées.
  - `suspicious_activity` : IP avec activités suspectes élevées.
  - `high_traffic_ips` : IP avec trafic anormalement élevé.

## Fonctionnement détaillé

1. **Lecture du fichier de log** :
   - Le fichier de log est lu ligne par ligne et chaque ligne est analysée à l'aide de la fonction `parse_log_line`.

2. **Analyse des logs** :
   - Les informations extraites sont utilisées pour :
     - Compter le trafic par IP.
     - Identifier les tentatives de connexion échouées (code de statut 401).
     - Identifier les accès à des URLs suspectes (par exemple, `/admin`, `/login`, `/wp-admin`, `/phpmyadmin`).
     - Compter les codes de statut HTTP.

3. **Identification des activités suspectes** :
   - Les IP avec un nombre élevé de tentatives de connexion échouées, un accès élevé à des URLs suspectes, ou un trafic anormalement élevé sont identifiées et listées séparément.


Ce script fournit un moyen efficace d'analyser les logs d'un serveur web pour détecter des activités suspectes et identifier les IP potentiellement malveillantes.
