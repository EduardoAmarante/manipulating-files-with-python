from pathlib import Path
import shutil

def move(nameFolder,filename):
    # moves files from the desktop to the path specified by the nameFolder variable
    shutil.move(filename, "C:/Users/{}/{}/{}".format(user,nameFolder, filename.name))
    print("Moving the file... {}".format(filename.name)) 

def analyze_and_move():
    # loop that checks all files in path(desktop)
    for filename in path.glob('*'):
        # checks if the file format is present in one of the lists
        # when it is present it sends the file to the directory named in the
        # first argument of move()
        if filename.suffix in formatoImages:
            move('Pictures',filename)
        elif filename.suffix in formatosDocs:
            move('Documents',filename)
        elif filename.suffix in formatoVideo:
            move('Videos',filename)
        elif filename.suffix in formatoDownloads:
            move('Downloads',filename)
           
# define your windows user here
user = 'eamar'

# lists organized according to the types of files to be handled
formatosDocs = ['.odt','.docx','.pptx','.xlsx','.ods','.csv','.pdf']
formatoImages = ['.jpg','.jpeg','.JPG','.JPEG','.png','.xcf','.HEIC']
formatoVideo = ['.MP4','.mp4','.mkv','.mlt','.MOV','.HVEC']
formatoDownloads = ['.zip','.exe']

# generates the Path to be compatible with shutil
path = Path("C:/Users/{}/Desktop/".format(user))

# runs the script
analyze_and_move()