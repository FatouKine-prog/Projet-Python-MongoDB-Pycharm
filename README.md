Toilettes publiques à Paris

Présentation

Ce projet permet de rechercher et afficher sur une carte les toilettes publiques situées à proximité d’une adresse à Paris.
Les données proviennent de Paris Open Data et sont stockées dans une base MongoDB.
L’utilisateur saisit une adresse, le programme récupère ses coordonnées GPS, calcule la distance avec les toilettes enregistrées dans la base, puis affiche sur une carte les équipements situés à moins de 700 mètres.


Objectifs du projet

• Utiliser une base de données issue de Paris Open Data
• Stocker et exploiter les données avec MongoDB
• Se connecter à MongoDB depuis Python avec Pycharm
• Géocoder une adresse avec Geopy / Nominatim
• Calculer la distance entre deux coordonnées GPS
• Afficher les résultats sur une carte interactive avec Folium

Fonctionnalités

• Saisie d’une adresse à Paris
• Conversion de l’adresse en latitude et longitude
• Recherche des toilettes publiques dans MongoDB
• Calcul de la distance entre l’utilisateur et chaque toilette
• Affichage uniquement des toilettes situées à moins de 700 m
• Affichage d’un cercle représentant la zone de recherche
• Marqueurs de couleur selon le statut :
  • Vert : en service
  • Rouge : autre statut
• Informations disponibles dans les popups :
  • type
  • adresse
  • arrondissement
  • statut
  • horaires
  • accès PMR
  • relais bébé
  • distance
• Lien vers Google Street View


Technologies utilisées

• Python
• MongoDB
• Navicat
• PyCharm
• PyMongo
• Folium
• Geopy / Nominatim
• HTML pour la carte générée


Base de données

Base MongoDB utilisée :
Database : toilettes_paris_db
Collection : toilettesparis

Le document contient notamment les champs suivants :
type
statut
adresse
arrondissement
horaire
acces_pmr
relais_bebe
geo_point_2d


Installation

Installer les bibliothèques nécessaires
MongoDB doit être lancé sur le port local par défaut :
mongodb://localhost:27017/


Utilisation

Lancer le fichier Python :
python toilettes_paris.py

Puis saisir une adresse, par exemple :
10 rue de Rivoli

Le programme :
Adresse saisie
Géocodage avec Geopy
Coordonnées GPS
Lecture des données MongoDB
Calcul des distances
Sélection des toilettes à moins de 700 m
Création de la carte Folium
toilettes_paris.html
La carte est ensuite enregistrée dans :
toilettes_paris.html
et ouverte automatiquement dans le navigateur.


Source des données

Les données utilisées proviennent du portail Paris Open Data, dataset des toilettes publiques de Paris.

Résultat

Le projet permet d’obtenir rapidement une carte interactive des toilettes publiques proches d’une adresse parisienne, avec les principales informations utiles sur chaque équipement.

Voici un aperçu de l'application

Saisie d'un adresse:

<img width="329" height="447" alt="Capture d&#39;écran 2026-09-24 195737" src="https://github.com/user-attachments/assets/dc74ee46-15f3-4005-b041-14a43f23c3fb" />



Les toilettes disponibles à moins de 700m de ma position:

<img width="598" height="487" alt="image" src="https://github.com/user-attachments/assets/7338b6ae-7562-4604-b66b-69cdc5dbea15" />



Ma position:

<img width="497" height="349" alt="Capture d&#39;écran 2026-09-24 200116" src="https://github.com/user-attachments/assets/ad4a8f99-42a8-4a2b-af4a-bec9e40a4369" />



Les informations de la toilette sélectionnée:

<img width="415" height="294" alt="image" src="https://github.com/user-attachments/assets/23350fa4-642b-48ea-aaab-f78efad002fe" />



Le Street View de la toilette sélectionnée:

<img width="514" height="470" alt="image" src="https://github.com/user-attachments/assets/8da14cac-23dc-483f-8369-e4fff1551c49" />


