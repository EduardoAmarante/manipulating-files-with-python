from pathlib import Path
import shutil

def move(nameFolder,filename):
    # move os arquivos da area de trabalho para o caminho especificado
    shutil.move(filename, "C:/Users/{}/{}/{}".format(user,nameFolder, filename.name))
    print("Moving the file... {}".format(filename.name)) 

def analyze_and_move():
    # loop que verifica todos arquivos do path
    for filename in path.glob('*'):
        #verifica se o formato de arquivo esta presente em uma das listas
        # quando estiver presente ele envia o arquivo para o diretorio nomeado no
        # primeiro argumento do move()
        if filename.suffix in formatoImages:
            move('Pictures',filename)
        elif filename.suffix in formatosDocs:
            move('Documents',filename)
        elif filename.suffix in formatoVideo:
            move('Videos',filename)
        elif filename.suffix in formatoDownloads:
            move('Downloads',filename)
           
# defina aqui seu usuario windows
user = 'eamar'

# listas organizadas de acordo com os tipos de arquivos a serem manipulados
formatosDocs = ['.odt','.docx','.pptx','.xlsx','.ods','.csv','.pdf']
formatoImages = ['.jpg','.jpeg','.JPG','.JPEG','.png','.xcf','.HEIC']
formatoVideo = ['.MP4','.mp4','.mkv','.mlt','.MOV','.HVEC']
formatoDownloads = ['.zip','.exe']

# gera o Path para ser compativel com o shutil
path = Path("C:/Users/{}/Desktop/".format(user))

# funcao principal que roda o script
analyze_and_move()