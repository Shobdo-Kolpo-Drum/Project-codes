from __future__ import print_function
ch=['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ', 'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়', 'ৎ', 'ং', 'ঃ', 'ঁ', ';', '”', '!', '।', '–', '=', '‘', '’', '[', ']', '*', '“', '?', '্ ', '/', ':', ', ', '.', '(', ')', 'া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ', 'ক্ষ', 'জ্ঞ', '2', '3', '4', '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
braille=[1, 345, 24, 35, 136, 1256, 5.1235, 15, 34, 135, 246, 13, 1346, 1245, 126, 346, 14, 16, 245, 1356, 25, 23456, 2456, 1246, 123456, 3456, 2345, 1456, 145, 2346, 1345, 1234, 124, 12, 1236, 134, 13456, 1235, 123, 146, 12346, 234, 125, 12456, 12356, 26, 2.2345, 56, 6, 3, 23, 356, 235, 256, 36, 56.2356, 6.236, 356.3, 6.2345, 2345.6, 35.35, 236, 236, 356, 34, 36, 2, 2, 2356, 2356, 345, 24, 35, 136, 1256, 5.1235, 15, 34, 135, 246, 12345, 156, 4, 46, 46, 3456.245, 3456.1, 3456.12, 3456.14, 3456.145, 3456.15, 3456.124, 3456.1245, 3456.125, 3456.24,]

word='রাফিয়া'
def split(word):
    return [char for char in word]
sr=split(word)
print(sr)

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list
indd=get_index_positions(sr,'্')


#jukto borno

 #2 letter   
for i in range(0,len(indd)):
#for the last item
    if i==len(indd)-1:
        sr.insert(indd[i]-1,'2')
        sr.pop(indd[i]+1)
        break

            
    if indd[i+1]!=indd[i]+2:
        sr.insert(indd[i]-1,'2')
        sr.pop(indd[i]+1)
    if indd[i+1]==indd[i]+2:
        sr.insert(indd[i]-1,'2')
        sr.pop(indd[i]+1)
# 4letter
ind=get_index_positions(sr,'2')
inde=get_index_positions(sr,'2')

for i in range(0,len(ind)-2):
    if ind[i]+2==ind[i+1]:
        if i==len(indd):
            
            break
        
        if ind[i]+4==ind[i+2]:
            sr[ind[i]]='4'
            inde.remove(inde[i+1])
            inde.remove(inde[i+1])

            

              

final_list = list(set(ind) - set(inde))
final_list.sort(reverse=True)

for i in final_list:
    sr.pop(i)
 # 3 letter

ind=get_index_positions(sr,'2')
inde=get_index_positions(sr,'2')
for i in range(0,len(ind)-1):     
    if ind[i]+2==ind[i+1]:
                sr[ind[i]]='3'
                if i+1<len(inde):
                    inde.remove(inde[i+1])


        
                
final_list = list(set(ind) - set(inde))
final_list.sort(reverse=True)
for i in final_list:
    sr.pop(i)


rakiba=[]
for cha in sr:
    if cha==' ':
        continue
    if cha in sr:
        index=ch.index(cha)
        if '.' in str(braille[index]):
            x = str(braille[index]).split(".")
            a=int(x[0])
            b=int(x[1])

            rakiba.append(a)
            rakiba.append(b)
        else:
            rakiba.append(braille[index])
print(sr)
print(rakiba)



    
       


        

  

    


        
    




       
    
        

        



