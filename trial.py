import csv
import os

# Create a dictionary to map positions to scores
position_scores = {
    '1': 8,
    '2': 7,
    '3': 6,
    '4': 5,
    '5': 4,
    '6': 3,
    '7': 2,
    '8': 1,
    '9': 1,
    '10': 1,
    '11': 1,
    '12': 1,
    '13': 1,
    'DNS': 0,
    'DQ': 0,
    '': 0
}

# Define the directory path
directory_path = r'C:\Users\lisia\Downloads\WakaNats2018'
directory_path = r'C:\Users\lisia\Downloads\WakaNats2017'

# Create a dictionary to store total scores for each name
total_scores_by_name = {}

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if os.path.isfile(os.path.join(root, file)) and os.path.splitext(file)[1].endswith('.csv') and 'Final' in file:
            with open(os.path.join(root, file), 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                
                for row in reader:
                    position = row[0]
                    name = row[5]
                    
                    if position in position_scores:
                        score = position_scores[position]
                    else:
                        score = 0
                    
                    if name not in total_scores_by_name:
                        total_scores_by_name[name] = 0
                    total_scores_by_name[name] += score

# Print the total scores for each name
for name, total_score in total_scores_by_name.items():
result =('Total score for', name, 'is', total_score)
