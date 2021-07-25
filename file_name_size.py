#!/usr/bin/env python
# coding: utf-8

# In[77]:


import os


# In[78]:


temp = os.listdir("D:/ASR_Bangla/audio_files_all_flac/asr_bengali_2/bangla_audio_files_2/29")


# In[80]:


name_size_list = []
for file in temp:
  name_size_list.append((file, os.stat("D:/ASR_Bangla/audio_files_all_flac/asr_bengali_2/bangla_audio_files_2/29/"+file).st_size))


# In[81]:


import pandas as pd
df = pd.DataFrame(name_size_list, columns=["FILENAME", "FILESIZE"])
df.to_csv('D:/ASR_Bangla/audio_files_all_flac/asr_bengali_2/name_size_csv/name_size_list_29.csv', index=False)


# In[82]:


name_size_list


# In[ ]:




