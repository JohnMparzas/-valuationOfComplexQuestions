import random
import sys
import csv
import time


time0=time.time()
f = open("output1,1.txt", "w+",encoding='utf-8')
f.write('primaryTitle'+'\t'+'directors'+'\n' )

with open('title.crew2.tsv',encoding='utf-8') as crew:
     crew=csv.reader(crew,delimiter='\t')
     
     with open('title.basics2.tsv',encoding='utf-8') as basics:
                         
          basics=csv.reader(basics,delimiter='\t')
          next(basics)
          basics_line=next(basics,False) 
          for crew_line in crew:
               #print(crew_line[0],' ',crew_line[1],' ',crew_line[2])
               
               directors=crew_line[1]
               
               if( ',' in directors):
                    crew_tconst=crew_line[0]
                    
                      
                    while(basics_line and basics_line[0]<=crew_tconst):
                             
                         basics_tconst=basics_line[0]
                    
                         if(basics_tconst==crew_tconst):
                              #print('brhka!!!!!!')
                                   
                              primary_title=basics_line[2]
                              #result[primary_title]=directors
                              f.write(str(primary_title)+'\t'+str(directors)+'\n' )
                             
                         basics_line=next(basics,False)
                             
duration=time.time()-time0
print('Experiment 1.1 \n')
print('execute time : ',duration,' sec')
f.close()
print('Done!')
