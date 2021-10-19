from pathlib import Path
import os,shutil, ctypes

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
            try:

                verificaPasta("G:/Meu Drive/{}".format(filename.suffix)) 
                shutil.move(filename, "G:/Meu Drive/{}/{}".format(filename.suffix,filename.name))
            except WindowsError:
                ctypes.windll.user32.MessageBoxW(0, "O arquivo esta sendo utilizado por outro processo", "Erro no Script", 0)

        else:
            print("não esta na lista")

with open("C:/Users/Eduardo/Desktop/config/tipos.txt") as file:
    for line in file:
        listaformatos.append(line.replace("\n",""))       
    
mover(listaformatos)