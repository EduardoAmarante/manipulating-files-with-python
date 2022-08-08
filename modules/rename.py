from pathlib import Path
import os,shutil, ctypes

p = 'D:/Filmes/SERIES/Breaking Bad/Season 04/'
path = Path(p)
acrescimo = 's04e'

for filename in path.glob('*'):
    print(filename)
    if filename.suffix == '.mp4':
        name = filename.name
        os.rename(p + name, p + acrescimo + name)
        print(name)
        
