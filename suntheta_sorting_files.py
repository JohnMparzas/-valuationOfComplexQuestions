import random
import sys
import csv

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

#'name.basics.tsv','title.akas.tsv','title.principals.tsv'
file_names=['title.basics.tsv','title.crew.tsv','title.episode.tsv','title.ratings.tsv']
for file in file_names:
     
     df = pd.read_csv(file, sep="\t")
     
     first_col=df.columns[0]
     df.sort_values(by='tconst',ascending=True, inplace = True)
     
     name=file.split('.')
     new_file_name=str(name[0])+'.'+str(name[1])+str(2)
     
     df.to_csv(str(new_file_name)+'.tsv', index = False, header=True,sep="\t")
     
     print('Done ',file)
     
print('Done!')

np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
