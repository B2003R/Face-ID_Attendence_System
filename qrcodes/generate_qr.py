import qrcode
import os

path = 'faces'
mylist = os.listdir(path)
for cl in mylist:
    name = os.path.splitext(cl)[0]
    qr = qrcode.make(name)
    qr.save()