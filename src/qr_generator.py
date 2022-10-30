import time
from modules import *

print('')
print('*')
time.sleep(.2)
print('**')
time.sleep(.2)
print('***')
time.sleep(.2)
print('')

print('"ENTER" to make a QR-Code with your WiFi network.')
time.sleep(1)
print('"1" to make an empty QR-Code...')

option = input('...> ')
print('')

if len(option) == 0:
	ConnectedSSID()

elif option == '1':
	name = input('Enter a name to save your file (whitout the ".png"): ')
	ssid = input('Type your wifi SSID: ')
	auth = input('Type your type of connection (example "WPA","WEP",etc...): ')
	password = input('Type your wifi password: ')
	AnotherQR(name,ssid,auth,password)

else:
	time.sleep(.2)
	print('ERROR: Please enter a valid option!')