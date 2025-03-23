import cv2
import cv2.aruco as aruco
from math import *

# Charger le dictionnaire ARUCO
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# Créer les paramètres du détecteur ARUCO
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()


while True:
    print("v")
    # Lire le cadre de la caméra
    ret, frame = cap.read()

    # Détecter les marqueurs ARUCO
    corners, ids, rejectedCandidates = detector.detectMarkers(frame)

    # Dessiner les marqueurs détectés sur l'image
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    
    if len(corners) > 0:
        for markerCorner in corners:
            if ids%2==0:
                print(True)
            
                
    
    # Afficher l'image résultante
    cv2.imshow('ARUCO Detection', frame)

    # Sortir de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()