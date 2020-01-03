# from PIL import Image
#
# path = "/home/kinsozheng/Desktop/compare_voc/8bit_fix/EAD2020_semantic_00000.png"
#
# im = Image.open(path)
#
# im.show()

import cv2

im_read = cv2.imread("/home/kinsozheng/Desktop/data_augment/tmp/mask/randomColor0EAD2020_semantic_00001.png")

cv2.imshow('d', im_read)
cv2.waitKey(0)