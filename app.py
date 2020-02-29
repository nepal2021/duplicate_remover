import pandas as pd
from sys import argv
import time
start_time = time.time()
#python ("Enter the file you want to compelete.")
file_name = argv[1]
#print(file_name)
filter = ['company','phone']
print(type(file_name))
df = pd.read_csv(file_name)
print(df)

pf = df.drop_duplicates(subset=filter[0], keep='last')
#print(df)
fn = file_name.split('.')[0]
result = fn+'_filtered.csv'
pf.to_csv(result)

print("%s created!--- %s seconds ---" % (result,time.time() - start_time))