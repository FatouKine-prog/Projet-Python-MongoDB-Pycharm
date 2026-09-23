import folium
import pymongo
import webbrowser

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# ============================================================
# 1. CONNEXION A MONGODB
# ============================================================

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["toilettes_paris_db"]
mycol = mydb["toilettesparis"]


# ============================================================
# 2. GEOLOCALISATION DE L'ADRESSE SAISIE
# ============================================================

geolocator = Nominatim(
    user_agent="toilettes_paris_application"
)

adresse_user = input("Entrez une adresse à Paris : ")

# On ajoute Paris pour améliorer la recherche
location = geolocator.geocode(
    adresse_user + ", Paris, France"
)


# ============================================================
# 3. SI L'ADRESSE EST TROUVEE
# ============================================================

if location:

    latitude_user = location.latitude
    longitude_user = location.longitude

    print("Adresse trouvée :", adresse_user)
    print("Latitude :", latitude_user)
    print("Longitude :", longitude_user)


    # ========================================================
    # 4. CREATION DE LA CARTE FOLIUM
    # ========================================================

    m = folium.Map(
        location=[
            latitude_user,
            longitude_user
        ],
        tiles=None,
        zoom_start=16
    )


    # ========================================================
    # 5. FOND DE CARTE
    # ========================================================

    folium.TileLayer(
        tiles=(
            "https://server.arcgisonline.com/ArcGIS/rest/services/"
            "World_Street_Map/MapServer/tile/{z}/{y}/{x}"
        ),
        attr="Tiles © Esri",
        name="Esri World Street Map"
    ).add_to(m)


    # ========================================================
    # 6. MARQUEUR DE L'ADRESSE DE L'UTILISATEUR
    # ========================================================

    folium.Marker(

        location=[
            latitude_user,
            longitude_user
        ],

        popup=folium.Popup(
            f"""
            <div style="font-family: Arial; width: 220px;">
                <h3>Ma position</h3>
                <p>{adresse_user}</p>
            </div>
            """,
            max_width=300
        ),

        tooltip="Ma position",

        icon=folium.Icon(
            color="blue",
            icon="home"
        )

    ).add_to(m)


    # ========================================================
    # 7. CERCLE DE RECHERCHE DE 700 METRES
    # ========================================================

    folium.Circle(

        location=[
            latitude_user,
            longitude_user
        ],

        radius=700,

        popup="Zone de recherche : 700 mètres",

        fill=False

    ).add_to(m)


    # ========================================================
    # 8. RECUPERATION DES TOILETTES DANS MONGODB
    # ========================================================

    toilettes = mycol.find()

    compteur = 0


    # ========================================================
    # 9. PARCOURIR LES TOILETTES
    # ========================================================

    for toilette in toilettes:

        # Récupération des coordonnées GPS
        geo = toilette.get("geo_point_2d")


        # Vérifier que les coordonnées existent
        if geo:

            latitude_toilette = geo.get("lat")
            longitude_toilette = geo.get("lon")


            if latitude_toilette is not None and longitude_toilette is not None:


                # ====================================================
                # 10. CALCUL DE LA DISTANCE
                # ====================================================

                distance = geodesic(

                    (
                        latitude_user,
                        longitude_user
                    ),

                    (
                        latitude_toilette,
                        longitude_toilette
                    )

                ).meters


                # ====================================================
                # 11. GARDER UNIQUEMENT LES TOILETTES
                #     A MOINS DE 700 METRES
                # ====================================================

                if distance < 700:

                    compteur += 1


                    # ================================================
                    # 12. RECUPERATION DES INFORMATIONS
                    # ================================================

                    type_toilette = toilette.get(
                        "type",
                        "Non renseigné"
                    )

                    statut = toilette.get(
                        "statut",
                        "Non renseigné"
                    )

                    adresse = toilette.get(
                        "adresse",
                        "Adresse non renseignée"
                    )

                    arrondissement = toilette.get(
                        "arrondissement",
                        "Non renseigné"
                    )

                    horaire = toilette.get(
                        "horaire",
                        "Non renseigné"
                    )

                    acces_pmr = toilette.get(
                        "acces_pmr",
                        "Non renseigné"
                    )

                    relais_bebe = toilette.get(
                        "relais_bebe",
                        "Non renseigné"
                    )


                    # ================================================
                    # 13. COULEUR DU MARQUEUR SELON LE STATUT
                    # ================================================

                    if statut.lower() == "en service":

                        couleur = "green"

                    else:

                        couleur = "red"


                    # ================================================
                    # 14. LIEN GOOGLE STREET VIEW
                    # ================================================

                    street_view_url = (
                        "https://www.google.com/maps/@?api=1"
                        "&map_action=pano"
                        f"&viewpoint={latitude_toilette},"
                        f"{longitude_toilette}"
                    )


                    # ================================================
                    # 15. CREATION DE LA POPUP
                    # ================================================

                    msg_html = f"""

                    <div style="
                        font-family: Arial;
                        width: 270px;
                    ">

                        <h3 style="
                            color: #333;
                            margin-bottom: 10px;
                        ">
                            🚻 Toilettes publiques
                        </h3>


                        <p>
                            <b>Type :</b>
                            {type_toilette}
                        </p>


                        <p>
                            <b>Adresse :</b>
                            {adresse}
                        </p>


                        <p>
                            <b>Arrondissement :</b>
                            {arrondissement}
                        </p>


                        <p>
                            <b>Statut :</b>
                            {statut}
                        </p>


                        <p>
                            <b>Horaires :</b>
                            {horaire}
                        </p>


                        <p>
                            <b>Accès PMR :</b>
                            {acces_pmr}
                        </p>


                        <p>
                            <b>Relais bébé :</b>
                            {relais_bebe}
                        </p>


                        <p style="
                            font-weight: bold;
                        ">
                            Distance :
                            {int(distance)} mètres
                        </p>


                        <a
                            href="{street_view_url}"
                            target="_blank"

                            style="
                                display: inline-block;
                                background-color: #4285F4;
                                color: white;
                                padding: 8px 12px;
                                text-decoration: none;
                                border-radius: 4px;
                            "
                        >

                            Voir dans Street View

                        </a>

                    </div>

                    """


                    # ================================================
                    # 16. AJOUT DU MARQUEUR SUR LA CARTE
                    # ================================================

                    folium.Marker(

                        location=[
                            latitude_toilette,
                            longitude_toilette
                        ],

                        popup=folium.Popup(
                            msg_html,
                            max_width=300
                        ),

                        tooltip=(
                            f"{adresse} - "
                            f"{int(distance)} m"
                        ),

                        icon=folium.Icon(
                            color=couleur,
                            icon="info-sign"
                        )

                    ).add_to(m)


    # ========================================================
    # 17. AFFICHAGE DU NOMBRE DE TOILETTES TROUVEES
    # ========================================================

    print(
        compteur,
        "toilette(s) trouvée(s) à moins de 700 mètres."
    )


    # ========================================================
    # 18. AJOUT DU CONTROLE DES COUCHES
    # ========================================================

    folium.LayerControl().add_to(m)


    # ========================================================
    # 19. SAUVEGARDE DE LA CARTE
    # ========================================================

    m.save("toilettes_paris.html")

    print("Carte créée : toilettes_paris.html")


    # ========================================================
    # 20. OUVERTURE DANS LE NAVIGATEUR
    # ========================================================

    webbrowser.open("toilettes_paris.html")


# ============================================================
# 21. SI L'ADRESSE N'EST PAS TROUVEE
# ============================================================

else:

    print("Adresse non trouvée.")