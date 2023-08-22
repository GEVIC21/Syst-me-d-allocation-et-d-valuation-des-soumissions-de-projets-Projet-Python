# Système de soumission, d'allocation et d'évaluation de projet

Les collèges, universités ou tout autre établissement d'enseignement mènent des projets ou donnent des missions pour une meilleure compréhension de l'approche pratique du sujet dans le monde réel. Et le projet implique de nombreuses tâches comme l'évaluation de résumés ou de synopsis, la correction de thèse et la mise à jour du module proposé avec vos guides.

## TRAVAUX PROPOSÉS

1. Module d'inscription ou de connexion
2. Module de téléchargement/téléchargement
3. Module de soumission précédente
4. Module utilisateur
5. Ouvrez le module de projet
6. Module d'évaluation
7. Module d'administration

Ce projet aidera à construire un système collaboratif pour les étudiants ainsi que pour les professeurs.
pour effectuer des tâches liées à la mission/au projet. Ce système a surmonté tous les
processus traditionnel de soumission manuelle des résumés, synopsis ou tout autre projet
Documents. Il fournit également une plate-forme sur laquelle l'instructeur peut attribuer des tâches à ses
le groupe respectif et l'étudiant peuvent choisir leur groupe ainsi que leur projet
guide. Les tâches liées au projet ouvert peuvent être attribuées par le guide du projet et d'autres
les facultés peuvent donner leur avis si elles le souhaitent. Les étudiants peuvent télécharger directement leur
travaux proposés et la documentation sur ce système pour l’évaluation des travaux. Au
fin du semestre/année, en fonction des performances des étudiants, l'administrateur peut
générer un rapport pour les universitaires et la notation de l'étudiant.

## exigences:

1.

## comment exécuter

1. Téléchargez le code et conservez-le dans un répertoire ("moodle")
2. créez un autre répertoire avec le nom "Moodle_files" au même emplacement que "moodel".
   Vous pouvez modifier le nom de Moodle_files si vous le souhaitez, mais vous devrez également le modifier dans les paramètres.
   ce répertoire est destiné au stockage des fichiers et des images.
3. allez sur moodle/Moodlel/settings.py et donnez votre identifiant de messagerie et votre mot de passe à l'endroit requis
   3.1 Installer l'environnement Virtuel : python -m venv .nom_de_votre_env
4. exécutez : 'pip install -r requirements.txt' pour ajouter les dependances
5. exécutez la commande suivante :
   1. python manage.py makemigrations
   2. python manage.py migrer
   3. python manage.py createsuperuser
   4. python manage.py runserver
6. ouvrez localhost sur le navigateur Web.
