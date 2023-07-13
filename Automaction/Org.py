from pathlib import Path
import collections as cl
import os
import shutil
#pasta = 
#pasta = Path.cwd() 
#p = Path.cwd()
#print(f'Dir: {p}')
#with path.open(mode='r') as fid:
   # headers = [line.strip() for line in fid if line.startswith('#')]
#print('\n'.join(headers))
#pasta.read_text()
#print(pasta)

pasta = Path.cwd() / 'D:\Test\TESTE2'
#p = pasta.read_text()
#print(p)
lista = cl.Counter(p.suffix for p in pasta.iterdir())
file = cl.Counter(p.stem for p in pasta.iterdir())
print(lista)
print(file)

for f in lista:
    extensao = pasta.suffix 
    print(file)
    os.makedirs(pasta+'/'+extensao)
    shutil.move(pasta+'/'+f, pasta+'/'+extensao+'/'+f)