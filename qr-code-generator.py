import qrcode
qr = qrcode.QRCode()
message = input("Enter your text: ")
qr.add_data(message)
qr.print_ascii()
