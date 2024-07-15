# Description

Ce script en Python parcourt un répertoire spécifié et affiche des informations sur les fichiers qu'il contient, y compris leurs noms et tailles en octets. Il utilise la bibliothèque standard `os` pour effectuer les opérations sur le système de fichiers.

# Installation

Ce script utilise uniquement les bibliothèques standard de Python, il n'y a donc pas de dépendances supplémentaires à installer.

# Utilisation

```
python3 gest_file.py
```

Entrez ensuite le chemin du répertoire que vous souhaitez parcourir lorsque cela vous est demandé.

# Fonctions

### list_files_with_sizes(directory)

Cette fonction parcourt un répertoire spécifié et affiche des informations sur les fichiers qu'il contient.

- Paramètre :
  - `directory` : Le chemin du répertoire à parcourir.

- Fonctionnement :
  - Vérifie si le chemin du répertoire existe.
  - Parcourt les dossiers et sous-dossiers du répertoire spécifié.
  - Pour chaque fichier trouvé, affiche le nom du fichier et sa taille en octets.

- Exemple :
  Si vous entrez `/path/to/directory` comme chemin de répertoire, la fonction affichera les informations des fichiers contenus dans ce répertoire et ses sous-répertoires.

# Fonctionnement détaillé

1. **Vérification de l'existence du répertoire** :
   - La fonction commence par vérifier si le chemin spécifié existe. Si le chemin n'existe pas, un message d'erreur est affiché et la fonction retourne.

2. **Parcours des répertoires et sous-répertoires** :
   - Utilise `os.walk` pour parcourir récursivement le répertoire spécifié et ses sous-répertoires.
   - Pour chaque répertoire parcouru, le chemin du répertoire courant est affiché.

3. **Affichage des informations sur les fichiers** :
   - Pour chaque fichier trouvé, son chemin complet est construit en utilisant `os.path.join`.
   - La taille du fichier est obtenue avec `os.path.getsize`.
   - Le nom du fichier et sa taille en octets sont affichés.

4. **Gestion des exceptions** :
   - Si une erreur survient à tout moment pendant l'exécution de la fonction (par exemple, problèmes de permission, fichiers non accessibles, etc.), l'erreur est capturée et un message d'erreur est affiché.
