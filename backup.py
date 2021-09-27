from pathlib import Path
import os,shutil

listaformatos = []
path = Path("C:/Users/Eduardo/Desktop/")

def verificaPasta(caminho):
    try:
        os.mkdir(caminho)
    except OSError:
        None

def mover(listaformatos):
    for filename in path.glob('*'):
        
        if filename.suffix in listaformatos:

            verificaPasta("G:/Meu Drive/{}".format(filename.suffix)) 
            shutil.move(filename, "G:/Meu Drive/{}/{}".format(filename.suffix,filename.name))

        else:
            print("não esta na lista")

with open("C:/Users/Eduardo/Desktop/config/tipos.txt") as file:
    for line in file:
        listaformatos.append(line.replace("\n",""))       
    
mover(listaformatos)