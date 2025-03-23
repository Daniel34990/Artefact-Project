import cv2
import cv2.aruco as aruco
from math import *
from commandes import forward, left, right, backward, time
# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Créer les paramètres du détecteur ARUCO
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)


def impair():
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)

    # Lire le cadre de la caméra
    ret, frame = cap.read()
    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    if len(corners) > 0:
        
        for markerCorner in corners:
            if ids%2==1:
                return True
        
    
    return False

def pair():
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)

    # Lire le cadre de la caméra
    ret, frame = cap.read()
    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    if len(corners) > 0:
        
        for markerCorner in corners:
            if ids%2==0:
                return True
        
    
    return False



def distance():
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)

    # Lire le cadre de la caméra
    ret, frame = cap.read()
    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    if len(corners) > 0:
        
        for markerCorner in corners:
             # Extrait les cordonnées des coins
            c = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = c
            #Convertit les (x,y) en int
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            #Détermine la longueur des traits verticaux en pixels
            longueur_gauche=bottomLeft[1]-topLeft[1]
            longueur_droite=bottomRight[1]-topRight[1]
            longueurVerti=int(abs((longueur_droite+longueur_gauche)/2))
            #Détermine la longueur des traits horizontaux en pixels
            longueur_haut=topRight[1]-topLeft[1]
            longueur_bas=bottomRight[1]-bottomLeft[1]
            longueurHori=int(abs((longueur_haut+longueur_bas)/2))
            #Calcule la distance avec 682 pixels pour 15 cm de distance (règle de Trois)
            distanceVerti=15*682/(longueurVerti+0.0001)
            distanceHori=15*682/(longueurHori+0.0001)
            distance=min(distanceVerti,distanceHori)
            return distance
    return False


