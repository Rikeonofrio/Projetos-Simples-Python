from turtle import back
import qrcode

data = input('dado que sera transformado em qr code:')

qr  =qrcode.QRCode(version= 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'blue', back_color = 'black')

img.save('C:/Users/Rike/Desktop/game/myqrcode2.png')