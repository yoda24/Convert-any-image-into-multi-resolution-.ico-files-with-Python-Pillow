from PIL import Image
img = Image.open("icon.png")
img.save(
    "app.ico",
    format="ICO",
    sizes=[(16,16), (24,24), (32,32), (48,48), (64,64), (128,128), (256,256)]
)


