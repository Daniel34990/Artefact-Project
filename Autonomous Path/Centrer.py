import cv2
import cv2.aruco as aruco
from math import *
from commandes import forward, left, right, backward
# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Créer les paramètres du détecteur ARUCO
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)

def AbscisseCentre(m):
    # Extrait les cordonnées des coins
    c = m.reshape((4, 2))
    (topLeft, topRight, bottomRight, bottomLeft) = c
    #Convertit les (x,y) en int
    topRight = (int(topRight[0]), int(topRight[1]))
    bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
    bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    topLeft = (int(topLeft[0]), int(topLeft[1]))
    abscisse_Verti=abs((topRight[0]+topLeft[0])//2)
    abscisse_Hori=abs((topLeft[0]+bottomLeft[0])//2)
    abscisse=min(abscisse_Hori,abscisse_Verti)
    return abscisse

def Centrer():
    # Capturer la vidéo depuis la webcam (remplacez 0 par le numéro de votre caméra)
    cap = cv2.VideoCapture(0)
    # Lire le cadre de la caméra
    ret, frame = cap.read()
    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)
    if len(corners) > 0:
        for markerCorner in corners:
            a=AbscisseCentre(markerCorner)
            if (int(abs(640-a)>200)):
                if a>640:
                    forward(-0.4,-0.4,0.1)
                else:
                    forward(0.4,0.4,0.1)
                
        

Centrer()
        
