import sys
import csv
import time
import pandas as pd

print('experiment 2.1 \n')
print('Hashing version')
time0=time.time()
with open('title.ratings2.tsv',encoding='utf-8') as rating:
     rating_l=rating.readline()
     rating_l=rating.readline()
     
     #rating_lin=rating.readline()
     #rating_line=rating_lin.split('\t')
     hash_list=[0,0,0,0,0,0,0,0,0,0]
     while(rating_l):
          rating_line=rating_l.split('\t')
          average_rating_string=rating_line[1]
          #print(average_rating_string)
          average_rating=float(average_rating_string)
          
          average_rating=average_rating+0.9
          average_rating=int(average_rating)
          hash_list[average_rating-1]+=1
          rating_l=rating.readline()
          
duration=time.time()-time0
for i in range(10):
     print(str(i+0.1),' - ',str(i+1),' : ',hash_list[i])
print('Done!')
          
print('duration: ',duration,'sec','\n')

############## SORT FILE BY averageRating

df = pd.read_csv('title.ratings.tsv', sep="\t")
file='title.ratings.tsv'    

df.sort_values(by='averageRating',ascending=True, inplace = True)
     
name=file.split('.')
new_file_name=str(name[0])+'.'+str(name[1])+str(3)
     
df.to_csv(str(new_file_name)+'.tsv', index = False, header=True,sep="\t")
   
print('Sorting file Done  ',file,'\n')
###########################################

print('Sorting version \n')
time1=time.time()

with open('title.ratings3.tsv',encoding='utf-8') as rating:
     rating_l=rating.readline()
     rating_l=rating.readline()
     
     #rating_lin=rating.readline()
     #rating_line=rating_lin.split('\t')
     katwfli=1
     katwfli_sum=0
     while(rating_l):
          rating_line=rating_l.split('\t')
          average_rating_string=rating_line[1]
          #print(average_rating_string)
          average_rating=float(average_rating_string)
          if(average_rating<=katwfli):
               katwfli_sum= katwfli_sum+1
          else:
               print(str(round(katwfli-0.8999,1  )),' - ',str(katwfli),' : ',katwfli_sum)
               katwfli=katwfli+1
               katwfli_sum=1
               
          rating_l=rating.readline()
          
     print(str(katwfli-0.9),' - ',str(katwfli),' : ',katwfli_sum)


      
duration2=time.time()-time1
print("duration : ",duration2,'\n')

print('Done!\n')

deference=abs(duration2-duration)

if(duration2<duration):
     print('Sorting version needs less time from Hashing version with deference ',deference )

else:
     print('Hashing version needs less time from  Sorting version with deference ' ,deference)














