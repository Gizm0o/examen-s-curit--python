import os

def list_files_with_sizes(directory):
    try:
        # Pour vérifier si le chemin est valide
        if not os.path.exists(directory):
            print(f"Le répertoire '{directory}' n'existe pas.")
            return
        # Boucle pour parcourir les dossiers, avec une vérification pour se poser sur les fichiers et retourner leurs infos
        for root, dirs, files in os.walk(directory):
            print(f"Répertoire courant: {root}")
            # Vérification de fichier, si oui affiche le nom avec sa taille
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                print(f"-> Fichier: {file} - Taille: {file_size} octets")
    # Exception
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

directory = input("Rentrez le chemin voulu : ")
list_files_with_sizes(directory)

