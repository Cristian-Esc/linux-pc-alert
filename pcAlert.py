#!/usr/bin/python3
import os
import urllib.request
import requests


BOT_TOKEN = [BOT_TOKEN]
CHAT_ID = [CHAT_ID]

def read_proteccion_pc():
    with open('~/PROTECCION_PC.txt', 'r') as file:
        return file.read().strip()

proteccion_pc = read_proteccion_pc()
if proteccion_pc == 'true':
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False

    if connect():
        print("Conectado")
        message = "🚨 Alguien ha iniciado sesión en esta laptop 🚨"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        response = requests.get(url)
        #print(response.content)
    else:
        print("Desconectado")
