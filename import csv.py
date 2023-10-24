import csv
import os

for root, dirs, files in os.walk('C:\\Users\lisia\Downloads\WakaNats2018'):
#Putting the directory 
    for file in files:
        if os.path.isfile(os.path.join(root, file)) and os.path.splitext(file)[1].endswith('.csv') and 'Final' in file:
            with open(os.path.join(root, file), 'r') as f:
                reader = csv.reader(f)
                first_row = next(reader)
                position = {}
                for row in reader:
                #The sc
                    if row[0] in position.keys():
                        position[row[0]] = position[row[0]] + int(row[1])
                    else:
                        if row[0] == '1':
                            position['1'] = 8
                        else:
                            position[row[0]] = int(row[2])
                        if row[0] == '2':
                            position['2'] = 7
                        if row[0] == '3':
                            position['3'] = 6  
                        if row[0] == '4':
                            position['4'] = 5
                        if row[0] == '5':
                            position['5'] = 4
                        if row[0] == '6':
                            position['6'] = 3
                        if row[0] == '7':
                            position['7'] = 2
                        if row[0] == '8':
                            position['8'] = 1
                        if row[0] == '9':
                            position['9'] = 1
                        if row[0] == '10':
                            position['10'] = 1
                        if row[0] == '11':
                            position['11'] = 1
                        if row[0] == '12':
                            position['12'] = 1
                        if row[0] == '13':
                            position['13'] = 1
                        if row[0] == 'DNS':
                            position['DNS'] = 0
                        if row[0] == 'DQ':
                            position['DQ'] = 0
                        if row[0] == '':
                            position[''] = 0
                Name = ("{}".format(row[5]))  
                #I'm defining the group name
                for position, score in position.items():
                    print('The position',position,'The score', score,'of', Name)

                    
                    
                    
                    
                
                    
                    
                    
                    
                    
                
                    