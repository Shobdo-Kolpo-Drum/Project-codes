#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os, shutil

txt_path = "D:/ASR_Bangla/audio_files_all_flac/audio_03_part6/test.txt"
delim = ".wav"
src = "D:/ASR_Bangla/audio_files_all_flac/audio_files_a_f"
dest = "D:/ASR_Bangla/audio_files_all_flac/audio_03_part6/test"

# First, create a list and populate it with the files
# you want to find (1 file per row in myfiles.txt)
files_to_find = []
with open(txt_path, "r") as filestream:
    for line in filestream:
        currentline = line.split(",")
        for file in currentline:
            f=[]
            f = file.split('.')
            files_to_find.append(f[0])

for root, dirs, files in os.walk(src):
    for file in files:
        _file, ext = file.split('.')
        if _file in files_to_find:
            # If we find it, notify us about it and copy it it to C:\NewPath\
            shutil.copy(os.path.abspath(root + '/' + _file+'.'+ext), dest)
            
with open("D:/ASR_Bangla/audio_files_all_flac/audio_03_part6/output_test.txt", "w") as a:
    for path, subdirs, files in os.walk(r'D:/ASR_Bangla/audio_files_all_flac/audio_03_part6/test'):
       for filename in files:
         f = os.path.join(filename)
         a.write(str(f)+'\n')
        
copied_list="D:/ASR_Bangla/audio_files_all_flac/audio_03_part6/output_test.txt"
files_copied = []
with open(copied_list, "r") as filestream:
    for line in filestream:
        currentline = line.split(",")
        for file in currentline:
            f=[]
            f = file.split('.')
            files_copied.append(f[0])
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))
print(Diff(files_to_find,files_copied))
print("Finished!!!")
