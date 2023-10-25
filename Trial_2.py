import os
import csv

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

# Define the base directory path
base_directory = r'C:\Users\lisia\OneDrive\Documents\Year 13\DTP3'

# Get the year from the user
while True:
    year = input("Enter the year (2017 or 2018): ")
    if year in ('2017', '2018'):
        break
    else:
        print("Invalid year. Please enter '2017' or '2018'.")

# Create a dictionary to store total scores for each name
total_scores_by_name = {}

# Process the selected year's directory
directory_path = os.path.join(base_directory, f'WakaNats{year}')
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if os.path.isfile(os.path.join(root, file)) and os.path.splitext(file)[1].endswith('.csv') and 'Final' in file:
            print(f"Processing {year} file: {os.path.join(root, file)}")  # Print the file being processed

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

                    total_scores_by_name.setdefault(name, 0)
                    total_scores_by_name[name] += score

# Sort and print the total scores in decreasing order
sorted_scores = sorted(total_scores_by_name.items(), key=lambda x: x[1], reverse=True)
for name, total_score in sorted_scores:
    print(f'Total score for {name} is {total_score}')


