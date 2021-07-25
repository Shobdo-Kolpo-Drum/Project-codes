import wave
from os import listdir
from os.path import isfile, join
m = input("/Users/rowshanarabegum/Downloads/data 5-12/Data1/test")
onlyfiles = [f for f in listdir(m) if isfile(join(m, f))]
for i in onlyfiles:
   
    
    try:
        wave.open(m+'/'+i)
    except:
        print(f"\033[1;31;47m ERROR AT "+i)
        print(f"\033[0:37:40m")
        continue
print(f"\033[1;32;40m Except those All ok!!!")