# Instalar bibliotecas: opencv-python, mediapipe, cvzone


import cv2
from cvzone.HandTrackingModule import HandDetector


webcam = cv2.VideoCapture(0)

# Inicializa o rastreador de mãos

rastreador = HandDetector(detectionCon=0.8, maxHands=4)


while True:

    sucesso, imagem = webcam.read()  

    # Detecta as mãos no quadro

    maos, imagem_maos = rastreador.findHands(imagem)

    # Mostra o quadro com as marcações

    cv2.imshow('Projeto 4 - IA', imagem_maos)

    if cv2.waitKey(1) != -1:
        break


webcam.release()
cv2.destroyAllWindows()
