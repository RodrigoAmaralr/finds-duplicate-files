# Programa para verificar arquivos duplicados

import os
import shutil
import zlib
import hashlib
import re

pathBase =      '/mnt/Arquivos/Dropbox'
pathFiles = []
dAllFiles = {}
bypass = ['.dropbox.cache', 'svn', 'UnB']
#bypass = []

def listFiles(path):
    global pathFiles
    objts = os.listdir(path)
    for obj in objts:
        tobj = path + '/' + obj
        if os.path.isdir(tobj):
            path_Bypass = pathBypass(tobj)
            if not path_Bypass:
                listFiles(tobj)
        else:
            pathFiles.append(tobj)
            
def pathBypass(tobj):
    for item in bypass:
        if item in tobj:
            return True
    return False
    
def CalculaCRC(pathFiles):
    global dAllFiles
    
    for pathFile in pathFiles:
        try:
            print('Verificando o Arquivo: ' + pathFile)
            bFile = open(pathFile, "rb")
            File = bFile.read()
            CRC = hashlib.sha256(File).hexdigest()
            if CRC in dAllFiles:
                SalvaTXT('CRC: ' + CRC + '\n' + pathFile + '\n' + dAllFiles[CRC]+ '\n\n')
            else:
                dAllFiles[CRC] = pathFile
            bFile.close()
        except:
            print('ERRO no arquivo: ' + pathFile)
            print('ERRO no arquivo: ' + dAllFiles[CRC])
            SalvaTXT('ERRO no arquivo: ' + str(pathFile.encode('utf8')) + '\n' + '                 '+  str(dAllFiles[CRC].encode('utf8')) + '\n')
            #input('Pause')
        
def SalvaTXT(Valor):
    pathFile = pathBase + '/' + 'Files.txt'
    arquivo = open(pathFile, 'a')
    arquivo.write(str(Valor))
    arquivo.close()
    
def main():   
    listFiles(pathBase)
    CalculaCRC(pathFiles)

if __name__ == '__main__':
    main()