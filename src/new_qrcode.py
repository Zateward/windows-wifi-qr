import qrcode

wifi = input('Type your wifi SSID: ')
connection = input('Type your type of connection (example "WPA","WEP",etc...): ')
password = input('Type your wifi password: ')

wifi_format = 'WIFI:S:'+wifi+';T:'+connection+';P:'+password+";;"

qr = qrcode.QRCode(
	version=2,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=50,
	border=1,
	)

qr.add_data(wifi_format)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('001.png')