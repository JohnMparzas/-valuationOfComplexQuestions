import sys
import csv
import time

time0=time.time()
print('Experiment 2.2 \n')
with open('title.basics2.tsv',encoding='utf-8') as basics:
     
     basics_l=basics.readline()
     basics_l=basics.readline()
     
     with open('title.ratings2.tsv',encoding='utf-8') as rating:
          
          rating_l=rating.readline()
          rating_l=rating.readline()
          
          count_s_y={}
          sum_rating_s_y={}
          
          while(basics_l):
               
               basics_line=basics_l.split('\t')
               rating_line=rating_l.split('\t')
               #print(basics_line)
               #print(rating_line)
               basics_tconst=basics_line[0]
               if(len(basics_line)>5):
                    start_year=basics_line[5]
               else:
                    print(basics_line)
               
               #start_year=int(start_year)
               rating_tconst=rating_line[0]
               if(len(rating_line)>1):
                    average_rating=rating_line[1]
               else:
                    print('rating file ended!')
                    break
               
               if(basics_tconst==rating_tconst):
                    years=count_s_y.keys()
                    if(start_year in years):
                         count_s_y[start_year]+=1
                         sum_rating_s_y[start_year]+=float(average_rating)
                    else:
                         if(start_year!= "\\N"):
                              count_s_y[start_year]=1
                              sum_rating_s_y[start_year]=float(average_rating)
                         
                    basics_l=basics.readline()
                    rating_l=rating.readline()
               else:
                    
                    basics_l=basics.readline()         

                    
years=count_s_y.keys()
sorted_years=list(years)
sorted_years.sort()
duration=time.time()-time0
for i in sorted_years:
     
     print( 'year: ',str(i),' average rating: ',round(sum_rating_s_y[i]/count_s_y[i],1))
               
print('\n duration: ',duration,' sec')
