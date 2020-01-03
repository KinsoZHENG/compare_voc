from PIL import Image
im = Image.open('/home/kinsozheng/Desktop/compare_voc/image_tif/EAD2020_semantic_00006_{0}.tif')
im.convert("P")
im.save('test.png') # or 'test.tif'