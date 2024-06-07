import cv2
from cvzone.HandTrackingModule import HandDetector


webcam = cv2.VideoCapture(0)

# inicializa o rastreador de maos

rastreador = HandDetector(detectionCon=0.8, maxHands=4)


while True:

    sucesso, imagem = webcam.read()  

    # detecta as maos no quadro

    maos, imagem_maos = rastreador.findHands(imagem)

    # mostra o quadro com as marcacoes

    cv2.imshow('Projeto 4 - IA', imagem_maos)

    if cv2.waitKey(1) != -1:
        break


webcam.release()
cv2.destroyAllWindows()
