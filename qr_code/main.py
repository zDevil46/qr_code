import qrcode


website_link = input("Insert your link: ")
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img_name = input("Insert the name of your QR code: ")
img.save(img_name + ".png")
