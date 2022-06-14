import qrcode
img = qrcode.make('https://pypi.org/project/Pillow/')
type(img)  # qrcode.image.pil.PilImage
img.save('some_file.png')