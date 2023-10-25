import csv
import os
import tkinter as tk
import tempfile

# Create a dictionary to map positions to scores
#This displays that the rank and assign the points
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

# Create a dictionary to store total scores for each name
total_scores_by_name = {}

# Variable to store the total number of files processed
total_files_processed = 0

def process_directory(year, label):
    directory_path = os.path.join(base_directory, f'WakaNats{year}')
    
    global total_files_processed
    
    #Showing that the files has been processing and reading up the file
    for root, dirs, files in os.walk(directory_path):
        total_files = len(files)
        label.config(text=f'Processing {year} files...\nTotal Files: {total_files_processed}/{total_files}')    
    
        
        for file in files:
            if os.path.isfile(os.path.join(root, file)) and os.path.splitext(file)[1].endswith('.csv') and 'Final' in file:
                label.config(text=f'Processing {year} files...\nTotal Files: {total_files_processed}/{total_files}\nProcessing {file}')
                print(os.path.join(root, file)) #printing all the files that the program read.
                
                with open(os.path.join(root, file), 'r') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip the header row

                    for row in reader:
                        position = row[0] #This shows only read the first column as I only need that information
                        name = row[5] #This shows only read the sixth column as I only need that information

                        if position in position_scores:
                            score = position_scores[position]
                        else:
                            score = 0
                        #This shows that scores has been combined by their name 
                        total_scores_by_name.setdefault(name, 0)
                        total_scores_by_name[name] += score
                        
                total_files_processed += 1

def save_and_open_csv():
    # Sort and save the total scores to a temporary CSV file
    sorted_scores = sorted(total_scores_by_name.items(), key=lambda x: x[1], reverse=True)
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".csv") as temp_csv:
        writer = csv.writer(temp_csv)
        writer.writerow(['Name', 'Total Score'])
        writer.writerows(sorted_scores)
    
    # Open the saved CSV file using the default application
    os.system(f'start excel.exe "{temp_csv.name}"')  # Assumes Excel is installed

def main():
    root = tk.Tk()
    root.title("WAKA AMA NATIONALS") #This is the title for the program
    
    label = tk.Label(root, text="Select a year to process files") #This is a button to help the user to choose between two years 
    label.pack()
    
    def process_2017():
        global total_files_processed
        total_files_processed = 0
        process_directory('2017', label)
        label.config(text="Processing complete. Saving and opening the results...")
        root.update()
        save_and_open_csv()
    
    def process_2018():
        global total_files_processed
        total_files_processed = 0
        process_directory('2018', label)
        label.config(text="Processing complete. Saving and opening the results...")
        root.update()
        save_and_open_csv()

    button_2017 = tk.Button(root, text="Process 2017", command=process_2017)
    button_2017.pack()

    button_2018 = tk.Button(root, text="Process 2018", command=process_2018)
    button_2018.pack()

    root.mainloop()

def show_processed_files():
    # Create a new window to display processed files
    processed_window = tk.Toplevel()
    processed_window.title("Processed Files")
    
    processed_label = tk.Label(processed_window, text="Processed Files:")
    processed_label.pack()
    
    for file_name in total_files_processed:
        file_label = tk.Label(processed_window, text=file_name)
        file_label.pack()

if __name__ == "__main__":
    main()
