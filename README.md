# Projeet Medicalia

Groupe:

    - Alexandre Desbos
    - Bapstiste Griva

Medicalia est un modèle qui doit aider à la prédication maladie selon différents symptomes ou inversement. Nous avons utilisé le [dataset](https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms) qui contient des maladies avec pour chacune d'elles les symptomes associés et les traitements.

Le modèle à été entrainer avec le fichier TrainingMedicalia.ipynb sur google colab et publié sur hugginface afin d'être utilisé dans une interface web.


# Deploiement

L'application est une interface web crée avec Gradio qui utilise le model Medicalia. On peut facilement lancer l'application en local
```
python3 interface.py
```