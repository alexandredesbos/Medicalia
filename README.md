# Projet Medicalia

Groupe:

    - Alexandre Desbos
    - Baptiste Griva

Medicalia est un modèle qui doit aider à la prédication maladie selon différents symptomes ou inversement. Nous avons utilisé le [dataset](https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms) qui contient des maladies avec pour chacune d'elles les symptomes associés et les traitements.

Le modèle à été entrainer avec le fichier TrainingMedicalia.ipynb sur google colab et publié sur hugginface afin d'être utilisé dans une interface web.
Nous avons essayé de modifié le dataset en utilisant des données de type question/réponse pour avoir un meilleur modèle mais cela n'a pas été concluant.
Nous avons aussi essayé de faire des entrainement long mais ce n'était pas efficace pour avoir des meilleurs résultats. 
Le paramètre faisant varier la qualité du modèle de facon significative à été le learning rate.


# Deploiement

L'application est une interface web crée avec Gradio qui utilise le model Medicalia. On peut facilement lancer l'application en local
```
python3 interface.py
```