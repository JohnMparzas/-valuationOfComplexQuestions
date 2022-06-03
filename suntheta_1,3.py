
import sys
import csv
import time


time0=time.time()
f = open("output1,3.txt", "w+",encoding='utf-8')
f.write('primaryTitle'+'\n' )
sumi=1

with open('title.basics2.tsv',encoding='utf-8') as basics:
     
     basics_lin=basics.readline()
     basics_lin=basics.readline()
     
          
     
     with open('title.ratings2.tsv',encoding='utf-8') as rating:
          rating_lin=rating.readline()
          rating_lin=rating.readline()
          
          while(basics_lin):
               basics_line=basics_lin.split('\t')
               rating_line=rating_lin.split('\t')
     
     
               if(basics_line[0]==rating_line[0]):
                    basics_lin=basics.readline()
                    rating_lin=rating.readline()
               else:
                    f.write(basics_line[2]+'\n')
                    basics_lin=basics.readline()         
                    sumi=sumi+1

duration=time.time()-time0
          
print('Experiment 1.3 \n')
print('Duration : ',duration,' sec')
f.close()
print('Done!')
print('Wrote ',sumi,' lines')

