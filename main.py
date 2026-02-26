import cv2
import numpy as np

imagem = cv2.imread('mona_lisa.jpg')

print(imagem.shape)

img_sem_azul = imagem.copy()
img_sem_azul[:, :, 0] = 0
cv2.imwrite('mona_lisa_sem_azul.jpg', img_sem_azul)

img_sem_verde = imagem.copy()
img_sem_verde[:, :, 1] = 0
cv2.imwrite('mona_lisa_sem_verde.jpg', img_sem_verde)

img_sem_vermelho = imagem.copy()
img_sem_vermelho[:, :, 2] = 0
cv2.imwrite('mona_lisa_sem_vermelho.jpg', img_sem_vermelho)




