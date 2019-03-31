from PIL import Image

im = Image.open('/Users/zhangchenfang/Pictures/sheep.jpeg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/zhangchenfang/Pictures/sheep_thumbnail.jpeg', 'jpeg')