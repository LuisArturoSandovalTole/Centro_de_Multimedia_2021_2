#Autor: Sandoval Juárez Luis Arturo
#Licencia: MIT

import tkinter as tk  
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from vlc import Instance
import time
import os
import sys
import webbrowser

####################################################################################################################

class ReproduccionEnVLC: #Crea ReproduccionEnVLC
    def __init__(self):
        self.Repro = Instance('Bucle')#Lo generaremos en un Bucle

    def añadeLista(self,opcion):#Añade a la lista dependiendo el tipo de archivo
        self.mediaList = self.Repro.media_list_new()#Se crea una lista de reproducción nueva
       
        ruta = r"/home/pi/Desktop/SAJL_centromultimedia/archivos"
        archivos = os.listdir(ruta)#Se creara la lista de todos la direcccion de los archivos

        for s in archivos:#Se elige una opción y a partir de esa se mostraran los archivos de ese tipo
            if opcion==1:#Visualizar FOTOS
                if '.jpg' in str(s) or 'png' in str(s) or 'jpeg' in str(s):#Si el archivo es png ó jpeg, estará presente.
                    self.mediaList.add_media(self.Repro.media_new(os.path.join(ruta,s)))
        
            if opcion==2:#Visualizar VIDEOS
                if '.mp4' in str(s) or '.avi' in str(s):#Si el archivo es .avi ó .mp4, estará presente.
                    self.mediaList.add_media(self.Repro.media_new(os.path.join(ruta,s)))
        
            if opcion==3:#Escuchar Música
                if '.mp3' in str(s):#Si el archivo es .mp3 estará presente.
                    self.mediaList.add_media(self.Repro.media_new(os.path.join(ruta,s)))
                    
        self.listaRepro = self.Repro.media_list_player_new()#Lista de Reproducción Vacía creada en ReproduccionEnVLC
        self.listaRepro.set_media_list(self.mediaList)#Reemplaza la lista anterior, con la nueva.
        
####################################################################################################################
#Acciones de VLC
        
    def play(self):#Empieza a reproducir
        self.listaRepro.play()
    def next(self):#Siguiente
        self.listaRepro.next()
    def pause(self):
        self.listaRepro.pause()
    def previous(self):#Anterior
        self.listaRepro.previous()
    def stop(self):#Pausa
        self.listaRepro.stop()
        
def repMusica(opcion):
    
    reproduce.añadeLista(opcion)#Realiza lista de reproducción

    reproduce.play()#Se estará reproduciendo
    
    while reproduce.is_playing():#SI se esta ejecutando, no habrá una paso a la siguiente.
        time.sleep(1)

    reproduce.next()#Reproduce la siguiente.
    time.sleep(9)
    
####################################################################################################################
#Realización de Ventana
ventana = tk.Tk()#Se crea la ventana 
ventana.title("Centro Multimedia")#Nombre de la ventana
ventana.geometry("1280x720")#Dimensiones

#Realización de un Label
label1 = tk.Label(
    ventana,
    text='Selecciona la opción que deseas',#Texto
    bg="red",#Color del fondo
    fg="white",#Color de la letra
    font=("Arial",24,"bold")#Características del texto
)

label1.pack(#Posición
    ipadx=10,
    ipady=10,
    fill='x'
)

#Menu de Seleccón
style = ttk.Style()

try:
    style.theme_create( "seleccion", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [100, 0, 100, 0] } },#dimensiones del label
        "TNotebook.Tab": {
            "configure": {"padding": [90, 0],"font" : ('Arial', '16', 'bold'), "background": "#A9F5F2" },#Fondo de Todo
            "map":       {"background": [("selected", "#0404B4")],#Fondo de Color del Menú seleccionado
                          "expand": [("selected", [0, 0, 0, 0])] } } } ) #dimensiones del boton
    style.theme_use("seleccion")
except:
    
    style.theme_use("seleccion")

#Variable controlVentana que será llamada despúes
controlVentana=ttk.Notebook(ventana)

#Ventana 1 y fondo de color verde-Streaming de Vídeo
Streaming=tk.Frame(controlVentana,bg='#58FA58')#Fondo de color de la ventana 
controlVentana.add(Streaming,text='Streaming de Vídeo')#Nombre de la ventana
controlVentana.pack(expand=1, fill="y")#Expande sobre Y

#Ventana 2 y fondo de color verde-Música Digital
MD=tk.Frame(controlVentana,bg='#F7D358')#Fondo de color de la ventana 
controlVentana.add(MD, text='Música Digital')#Nombre de la ventana
controlVentana.pack(expand=1, fill="y")#Expande sobre Y

#Ventana 3 y fondo de color rosa-Archivos de USB
USB=tk.Frame(controlVentana,bg='#F6CEEC')#Fondo de color de la ventana
controlVentana.add(USB, text="Archivos de USB")#Nombre de la ventana
controlVentana.pack(expand=1, fill="y")#Expande sobre Y 
####################################################################################################################
#Icons de Streaming de Vídeo

#Icon de Nexflix
netflix = Image.open('net.png')#Dirección de la imagen 
netflix = netflix.resize((400,200),Image.ANTIALIAS)#Tamaño del cuadro de la imagen
netflix = ImageTk.PhotoImage(netflix)#Colocar imagen en Netflix
ttk.Button(Streaming,image=netflix,#Al momento de seleccionar te riderecciona a el link, ubicación del icon.
          command=lambda : webbrowser.open("http://www.netflix.com", new=2, autoraise=True)).pack(padx=20,pady=40)

#Icon de HBO-GO
hbo = Image.open('hbogo.png')#Dirección de la imagen
hbo = hbo.resize((400,200),Image.ANTIALIAS)#Tamaño del cuadro de la imagen
hbo = ImageTk.PhotoImage(hbo)#Colocar imagen en hbo
ttk.Button(Streaming,image=hbo,#Al momento de seleccionar te riderecciona a el link, ubicación del icon
          command=lambda : webbrowser.open("https://www.hbo.com", new=2,autoraise=False)).pack(padx=150,side="left")

#Icon de Blim
blim = Image.open('blim.png')#Dirección de la imagen
blim = blim.resize((400,200),Image.ANTIALIAS)#Tamaño del cuadro de la imagen
blim = ImageTk.PhotoImage(blim)#Colocar imagen en hbo
ttk.Button(Streaming,image=blim,#Al momento de seleccionar te riderecciona a el link, ubicación del icon
          command=lambda : webbrowser.open("http://www.blim.com", new=2,autoraise=True)).pack(padx=20,side="left")

####################################################################################################################
#Icons de Música Digital

#Icon de Spotify
spoti = Image.open('spoti.png')#Dirección de la imagen 
spoti = spoti.resize((400,200),Image.ANTIALIAS)#Tamaño del cuadro de la imagen
spoti = ImageTk.PhotoImage(spoti)#Colocar imagen en Netflix
ttk.Button(MD,image=spoti,#Al momento de seleccionar te riderecciona a el link, ubicación del icon.
          command=lambda : webbrowser.open("http://www.spotify.com", new=2, autoraise=True)).pack(padx=20,pady=40)

#Icon de Cloudfare
cloud = Image.open('cloud.png')#Dirección de la imagen
cloud = cloud.resize((400,200),Image.ANTIALIAS)#Tamaño del cuadro de la imagen
cloud = ImageTk.PhotoImage(cloud)#Colocar imagen en hbo
ttk.Button(MD,image=cloud,#Al momento de seleccionar te riderecciona a el link, ubicación del icon
          command=lambda : webbrowser.open("https://www.cloudflare.com", new=2,autoraise=False)).pack(padx=150,side="left")

####################################################################################################################
#Icons de USB


reproduce = ReproduccionEnVLC()#Reproduce llama a ReproduccionEnVLC

fotos = Image.open('fotos.png')
fotos = fotos.resize((180,180),Image.ANTIALIAS)
fotos = ImageTk.PhotoImage(fotos)
ttk.Button(USB,image=fotos,
           command=lambda : repMusica(1)).pack(padx=100,pady=0,side="left")

videos = Image.open('videos.png')
videos = videos.resize((180,180),Image.ANTIALIAS)
videos = ImageTk.PhotoImage(videos)
ttk.Button(USB,image=videos,
           command=lambda : repMusica(2)).pack(padx=100,pady=0,side="left")

musica = Image.open('musica.png')
musica = musica.resize((180,180),Image.ANTIALIAS)
musica = ImageTk.PhotoImage(musica)
ttk.Button(USB,image=musica,
           command=lambda : repMusica(3)).pack(padx=100,pady=0,side="left")

####################################################################################################################
#Icons de Reproducción

#Botón de Atras

atras = Image.open('retro.png')
atras = atras.resize((40,40),Image.ANTIALIAS)
atras = ImageTk.PhotoImage(atras)
ttk.Button(USB,image=atras,
           command=lambda : reproduce.previous()).pack(pady=10,side="bottom")#Se manda a llamar a la función reproduce

#Botón de Play/Pause

play = Image.open('play.png')
play = play.resize((40,40),Image.ANTIALIAS)
play = ImageTk.PhotoImage(play)
ttk.Button(USB,image=play,
           command=lambda : reproduce.play()).pack(pady=10,side="bottom")#Se manda a llamar a la función play/pause

#Botón de Stop

stop = Image.open('stop.png')
stop = stop.resize((40,40),Image.ANTIALIAS)
stop = ImageTk.PhotoImage(stop)
ttk.Button(USB,image=stop,
           command=lambda : reproduce.stop()).pack(pady=10,side="bottom")#Se manda a llamar a la función stop

#Botón de Siguiente

sig = Image.open('sig.png')
sig = sig.resize((40,40),Image.ANTIALIAS)
sig = ImageTk.PhotoImage(sig)
ttk.Button(USB,image=sig,
           command=lambda : reproduce.next()).pack(pady=10,side="bottom")#Se manda a llamar a la función next
 
ventana.mainloop()  