import cv2
import numpy as np

imagen = cv2.imread('gato.jpeg')

cv2.circle(imagen, (40,33),7,(255,0,0),2)
cv2.circle(imagen, (240,37),7,(0,255,0),2)
cv2.circle(imagen, (53,167),7,(0,0,255),2)
cv2.circle(imagen, (252,170),7,(255,255,0),2)

pts1 = np.float32([[40,33],[240,37],[53,167],[252,170]])
pts2 = np.float32([[0,0],[480,0],[0,300],[480,300]])

m = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(imagen,m,(480,300))

cv2.imshow('IMAGEN DE PRUEBA', imagen)
cv2.imshow('SALIDA',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()