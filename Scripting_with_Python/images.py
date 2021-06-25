from PIL import Image, ImageFilter

#Open Image using PIL.Image
with Image.open("./Scripting/img.jpg") as img:
    print(f'The Mode of img is {img.mode}')
    print(f'The format of img is {img.format}')
    print(f'The size of img is {img.size}')

    #Applying Image Filter
    filtered_img = img.filter(ImageFilter.BLUR)
    print(f'The Mode of filtered_img is {filtered_img.mode}')
    print(f'The format of filtered_img is {filtered_img.format}')
    print(f'The size of filtered_img is {filtered_img.size}')
    filtered_img.save("./images/blurred.png","png")

    #Converting mode from RGB to L (Black and white)
    black_white = img.convert('L')
    print(f'The Mode of black_white is {black_white.mode}')
    print(f'The format of black_white is {black_white.format}')
    print(f'The size of black_white is {black_white.size}')
    black_white.save("./images/blackwhite.png", "png")

    #Show Image
    filtered_img.show()

    #Rotate Image
    crooked = filtered_img.rotate(90)
    crooked.save("./images/crooked.png","png")

    #Resize Image
    resize = filtered_img.resize((600,900))
    print(resize.size)
    resize.save("./images/resized.png","png")

    #Crop Image
    top_left = (0,0)
    bottom_right = (100,800)
    cropped = resize.crop((*top_left, *bottom_right))
    cropped.save("./images/cropped.png","png")

with Image.open("/home/user1/Downloads/casper-van-battum-7B8mrPj9XsQ-unsplash.jpg") as img:
    print(img.size)
    #thumbnail method try to keep the aspect ratio while scaling down. 
    img.thumbnail((400,200))
    print(img.size)
    img.save("./images/thumbnail.png","png")