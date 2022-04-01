from pathlib import Path
import os,shutil, ctypes

listaformatos = []
formatosPlanilhas = ['.xlsx','.ods','.csv']
formatosDocs = ['.odt','.docx','.pptx']
formatoImages = ['.jpg','.jpeg','.JPG','.JPEG','.png']
path = Path("C:/Users/Eduardo/Desktop/")

def separarPorTipo(nomePasta,filename):
                try:
                    verificaPasta("D:/files/{}".format(nomePasta)) 
                    shutil.move(filename, "D:/files/{}/{}".format(nomePasta, filename.name))
                except WindowsError:
                    ctypes.windll.user32.MessageBoxW(0, "O arquivo esta sendo utilizado por outro processo", "Erro no Script", 0)

def verificaPasta(caminho):
    try:
        os.mkdir(caminho)
    except OSError:
        None

def mover(listaformatos):
    for filename in path.glob('*'):
        
        if filename.suffix in listaformatos:

            with open("C:/Users/Eduardo/Desktop/config/caminho.txt") as file:
                caminho = []
                for line in file:
                    caminho.append(line.replace("\n","")) 
            
            """ verificaPasta("{}/{}".format(caminho[0],filename.suffix)) 
            #verificaPasta("G:/Meu Drive/{}".format(filename.suffix)) 
            shutil.move(filename, "{}/{}/{}".format(caminho[0],filename.suffix,filename.name)) """

            if filename.suffix in formatosPlanilhas:
                separarPorTipo('Planilhas',filename)
            elif filename.suffix in formatosDocs:
                separarPorTipo('Documentos',filename)
            elif filename.suffix in formatoImages:
                separarPorTipo('Imagens',filename)
            else:
                separarPorTipo(filename.suffix,filename)
        else:
            print("não esta na lista")

with open("C:/Users/Eduardo/Desktop/config/tipos.txt") as file:
    for line in file:
        listaformatos.append(line.replace("\n",""))  
    
mover(listaformatos)