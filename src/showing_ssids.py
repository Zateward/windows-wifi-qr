import subprocess

data_prof_auth = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode('utf-8').split('\n')
data_password = subprocess.check_output(['netsh', 'wlan', 'show','profiles']).decode('utf-8').split('\n')

for profile in data_prof_auth:
	if profile.startswith('    Profile'):
		profile = profile[29:]
		profile = profile.split(' ')
		profile = profile[0]
		print('SSID:',profile)

		data_password = subprocess.check_output(['netsh', 'wlan', 'show','profiles', 'name='+profile, 'key=clear']).decode('utf-8').split('\n')
		#print(data_password)
		for password in data_password:
			if password.startswith('    Key Content'):
				password = password[29:]
				password = password.split(' ')
				password = password[0]
				print('Password:', password)

	else: continue

for auth in data_prof_auth:
	if auth.startswith('    Authentication'):
		auth = auth[29:32]
		auth = auth.split(' ')
		auth = auth[0]
		print('Authentication:', auth)

	else: continue