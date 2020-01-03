import os

import cv2
from PIL import Image
from natsort import natsort
from multiprocessing import Pool


def fix_eight_bit_problem(img_name):
    path = "/home/kinsozheng/Desktop/compare_voc/24bit_ori/" + img_name + ".png"
    img = Image.open(path)

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



    img = img.convert("P")
    error_save_path = "/home/kinsozheng/Desktop/compare_voc/8bit_error/" + img_name + ".png"
    img.save(error_save_path)

    img = Image.open(error_save_path)

    for coordinate in first:
        # print(coordinate)
        img.putpixel(coordinate, (0, 0, 128))

    for coordinate in second:
        # print(coordinate)
        img.putpixel(coordinate, (0, 128, 0))

    for coordinate in third:
        # print(coordinate)
        img.putpixel(coordinate, (0, 128, 128))

    for coordinate in forth:
        # print(coordinate)
        img.putpixel(coordinate, (128, 0, 0))

    for coordinate in fifth:
        img.putpixel(coordinate, (128, 0, 128))

    for coordinate in sixth:
        img.putpixel(coordinate, (255, 255, 255))

    for coordinate in seven:
        img.putpixel(coordinate, (0, 0, 0))

    correct_save_path = "/home/kinsozheng/Desktop/compare_voc/8bit_fix/" + img_name + ".png"
    img.save(correct_save_path)

if __name__ == '__main__':
    path = "/home/kinsozheng/Desktop/compare_voc/24bit_ori/"
    files = natsort.natsorted(os.listdir(path))

    file_names = []

    for file in files:
        name = os.path.splitext(file)[0]
        file_names.append(name)

    pool = Pool()
    pool.map(fix_eight_bit_problem, file_names)

    pool.close()
    pool.join()
