import csv
import os


# the directory
for roots, dirs, files in os.walk(r'C:\\lisia\Downloads\WakaNats2018'):
    for file in  files:
        if os.path.isfile(os.path.join(root,file)) and os.path.splitext(file)[1].endswith('.csv') and 'Final' in file:
            with open(os.path.join(root,file)) as f:
                reader = csv.reader(f)
                first_row = next(reader)
                
            
            
    
    