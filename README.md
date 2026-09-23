Toilettes publiques de Paris

Projet Python réalisé à partir des données Open Data Paris.

L'application permet de saisir une adresse à Paris et d'afficher sur une carte les toilettes publiques situées à moins de 700 mètres. 

Technologies utilisées
Python
MongoDB
PyCharm
Geopy
Folium

Base de données
Database : toilettes_paris_db
Collection : toilettesparis

Fonctionnement
L'utilisateur saisit une adresse.
Geopy récupère les coordonnées GPS.
Python lit les toilettes enregistrées dans MongoDB.
La distance entre l'adresse et chaque toilette est calculée.
Les toilettes situées à moins de 700 m sont affichées sur une carte Folium.
Les marqueurs indiquent le statut des toilettes :
🟢 En service
🔴 Autre statut
🔵 Position de l'utilisateur

Installation
python -m pip install pymongo folium geopy
Lancer le projet
python toilettes_paris.py
Une carte toilettes_paris.html est ensuite générée et ouverte dans le navigateur.

Source
Données : Open Data Paris – Toilettes publiques.
