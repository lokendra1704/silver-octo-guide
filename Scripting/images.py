from PIL import Image, ImageFilter

#Open Image using PIL.Image
img = Image.open("./Scripting/img.jpg")
print(f'The Mode of img is {img.mode}')
print(f'The format of img is {img.format}')
print(f'The size of img is {img.size}')

#Applying Image Filter
filtered_img = img.filter(ImageFilter.BLUR)
print(f'The Mode of filtered_img is {filtered_img.mode}')
print(f'The format of filtered_img is {filtered_img.format}')
print(f'The size of filtered_img is {filtered_img.size}')
filtered_img.save("blur.png","png")

#Converting mode from RGB to L (Black and white)
black_white = img.convert('L')
print(f'The Mode of black_white is {black_white.mode}')
print(f'The format of black_white is {black_white.format}')
print(f'The size of black_white is {black_white.size}')
black_white.save("blackwhite.png", "png")

#Show Image
filtered_img.show()