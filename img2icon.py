from PIL import Image

img = Image.open("image1.png").convert("RGBA") #make sure 4 channels

target_rgb = (255, 201, 14)

pixels = img.load()
for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        if (r, g, b) == target_rgb:
            pixels[x, y] = (255, 255, 255, 0) #set alpha to zero (transparancy)

img.save(
    "app.ico",
    format="ICO",
    sizes=[(16,16), (24,24), (32,32), (48,48), (64,64), (128, 128), (256, 256)])
