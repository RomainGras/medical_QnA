import json
import sys

# Remplace par le nom EXACT de du fichier notebook
notebook_filename = "medical_qna_project.ipynb" 

try:
    with open(notebook_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # On supprime la clé 'widgets' qui pose problème dans les métadonnées
    if 'widgets' in data.get('metadata', {}):
        del data['metadata']['widgets']
        print(f"Succès : La clé 'widgets' a été supprimée de {notebook_filename}")
        
        # On sauvegarde le fichier corrigé
        with open(notebook_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=1)
    else:
        print("Info : Pas de clé 'widgets' trouvée. Le fichier semble déjà propre.")

except FileNotFoundError:
    print(f"Erreur : Le fichier '{notebook_filename}' est introuvable.")
except Exception as e:
    print(f"Erreur : {e}")