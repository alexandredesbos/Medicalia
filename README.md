# Projet Medicalia

Groupe:

    - Alexandre Desbos
    - Baptiste Griva

Medicalia est un modèle qui doit aider à la prédication maladies selon différents symptomes ou inversement. Nous avons utilisé le [dataset](https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms) qui contient des maladies avec pour chacune d'elles les symptomes associés et les traitements.

Le modèle a été entrainer avec le fichier TrainingMedicalia.ipynb sur Google colab et publié sur hugginface afin d'être utilisé dans une interface web.
Nous avons essayé de modifier le dataset en utilisant des données de type question/réponse pour avoir un meilleur modèle mais cela n'a pas été concluant.
Nous avons aussi essayé de faire des entrainements longs mais ce n'était pas efficace pour avoir de meilleurs résultats. 
Le paramètre faisant varier la qualité du modèle de facon significative a été le learning rate.


# Deploiement

L'application est une interface web crée avec Gradio qui utilise le model Medicalia. On peut facilement lancer l'application en local
```
python3 interface.py
```