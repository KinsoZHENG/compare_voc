import cv2
from PIL import Image

img = Image.open("/home/kinsozheng/Desktop/compare_voc/image_own/EAD2020_semantic_00000.png")

im_read = cv2.imread("/home/kinsozheng/Desktop/compare_voc/image_own/EAD2020_semantic_00000.png", -1)
cv2.imshow('d', im_read)
cv2.waitKey(0)

print(img.format, img.size, img.mode)
# img.show()
print(img.size[0], img.size[1])

first = []
second = []
third = []
forth = []
fifth = []
sixth = []
seven = []

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r, g, b = img.getpixel((x, y))
        if (r, g, b) == (0, 0, 128):
            first.append((x, y))

        if (r, g, b) == (0, 128, 0):
            second.append((x, y))

        if (r, g, b) == (0, 128, 128):
            third.append((x, y))

        if (r, g, b) == (128, 0, 0):
            forth.append((x, y))

        if (r, g, b) == (128, 0, 128):
            fifth.append((x, y))

        if (r, g, b) == (255, 255, 255):
            sixth.append((x, y))

        if (r, g, b) == (0, 0, 0):
            seven.append((x, y))
        # img.putpixel((x, y), (int(r / 2), int(g / 2), int(b / 2)))

print(first)
print(second)
print(third)
print(forth)
print(fifth)
print(sixth)

img = img.convert("P")
img.save("temp.png")

img = Image.open("temp.png")

for coordinate in first:
    print(coordinate)
    img.putpixel(coordinate, (0, 0, 128))

for coordinate in second:
    print(coordinate)
    img.putpixel(coordinate, (0, 128, 0))

for coordinate in third:
    print(coordinate)
    img.putpixel(coordinate, (0, 128, 128))

for coordinate in forth:
    print(coordinate)
    img.putpixel(coordinate, (128, 0, 0))

for coordinate in fifth:
    img.putpixel(coordinate, (128, 0, 128))

for coordinate in sixth:
    img.putpixel(coordinate, (255, 255, 255))

for coordinate in seven:
    img.putpixel(coordinate, (0, 0, 0))

print(img.format, img.size, img.mode)
img.save("temp2.png")
# img.show()
im_read = cv2.imread("temp2.png")
cv2.imshow('s', im_read)
cv2.waitKey(0)
