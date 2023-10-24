import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

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

def process_directories(directory_paths):
    total_scores_by_name = {}

    for directory_path in directory_paths:
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

    return total_scores_by_name

def show_results(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    result_text.delete('1.0', tk.END)
    for name, total_score in sorted_scores:
        result_text.insert(tk.END, f'Total score for {name} is {total_score}\n')

def process_button_click():
    selected_directories = filedialog.askdirectory(multiple=True)
    if selected_directories:
        scores = process_directories(selected_directories)
        show_results(scores)
    else:
        messagebox.showinfo("Information", "No directories selected.")

# Create the main application window
app = tk.Tk()
app.title("Score Processing GUI")

# Create and place widgets
process_button = tk.Button(app, text="Process Directories", command=process_button_click)
process_button.pack(padx=20, pady=10)

result_text = tk.Text(app, height=10, width=40)
result_text.pack(padx=20, pady=10)

# Start the GUI event loop
app.mainloop()
