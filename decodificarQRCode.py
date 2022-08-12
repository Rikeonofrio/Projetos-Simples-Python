from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/Rike/Desktop/game/myqrcode.png')

result = decode(img)

print(result)