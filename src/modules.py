import subprocess
import qrcode

def ConnectedSSID():
	try:
		data_prof_auth = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode('utf-8').split('\n')
		data_password = subprocess.check_output(['netsh', 'wlan', 'show','profiles']).decode('utf-8').split('\n')

		for profile in data_prof_auth:
			if profile.startswith('    Profile'):
				profile = profile[29:]
				profile = profile.split(' ')
				profile = profile[0]
				print('SSID:',profile)

				for auth in data_prof_auth:
					if auth.startswith('    Authentication'):
						auth = auth[29:32]
						auth = auth.split(' ')
						auth = auth[0]
						print('Authentication:', auth)

						data_password = subprocess.check_output(['netsh', 'wlan', 'show','profiles', 'name='+profile, 'key=clear']).decode('utf-8').split('\n')
						#print(data_password)

						for password in data_password:
							if password.startswith('    Key Content'):
								password = password[29:]
								password = password.split('\r')
								password = password[0]
								print('Password:', password)

								wifi_format = 'WIFI:S:'+profile+';T:'+auth+';P:'+password+";;"

								qr = qrcode.QRCode(
									version=2,
									error_correction=qrcode.constants.ERROR_CORRECT_L,
									box_size=50,
									border=1,
									)

								qr.add_data(wifi_format)
								qr.make(fit=True)

								img = qr.make_image(fill_color='black', back_color='white')
								img.save(profile+'.png')

	except:
		print('ERROR, BITCH')




def AnotherQR(name,ssid, auth, password):
	wifi_format = 'WIFI:S:'+ssid+';T:'+auth+';P:'+password+";;"

	qr = qrcode.QRCode(
		version=2,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=50,
		border=1,
		)

	qr.add_data(wifi_format)
	qr.make(fit=True)

	img = qr.make_image(fill_color='black', back_color='white')
	img.save(name+'.png')