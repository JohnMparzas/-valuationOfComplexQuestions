import random
import sys
import csv
import time


time0=time.time()
f = open("output1,2.txt", "w+",encoding='utf-8')
f.write('primaryTitle'+'\t'+'directors'+'\n' )
sumi=0

with open('title.episode2.tsv',encoding='utf-8') as episode:
     episode=csv.reader(episode,delimiter='\t')
     next(episode)
     with open('title.basics2.tsv',encoding='utf-8') as basics:
          basics=csv.reader(basics,delimiter='\t')
          next(basics)
          basics_line=next(basics,False)
          for episode_line in episode:
          
               if(episode_line[3]=='1'):
                    episode_tconst = episode_line[0]
                    parent_tconst = episode_line[1]
                    seasonNumber = episode_line[2]
                    
                    
                    while(basics_line and basics_line[0]<=episode_tconst):
                         
                         basics_tconst = basics_line[0]
                         
                         if(basics_tconst==episode_tconst):
                              
                              primary_title=basics_line[2]
                              f.write(str(primary_title)+'\t'+str(parent_tconst)+'\t'+str(seasonNumber)+'\n' )
                         basics_line=next(basics,False)

duration=time.time()-time0
print('Experiment 1.2 \n')
print('duration ',duration,' sec')
f.close()
print('Done!')

