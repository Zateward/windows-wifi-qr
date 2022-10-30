# this is a program to test the wifi code, to leter put in in the qr generator.

# setting up the variables.
wifi = input('Type your wifi SSID: ')
connection = input('Type your type of connection (example "WPA","WEP",etc...): ')
password = input('Type your wifi password: ')

wifi_format = 'WIFI:S:'+wifi+';T:'+connection+';P:'+password+";;"
print(wifi_format)