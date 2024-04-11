import tkinter as tk
from tkinter import filedialog
import csv

def print_csv_with_index(file_path, searchKey, dateKey=None, output_directory=None):
    timeList = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            if searchKey in row[0]:
                if dateKey is None or dateKey in row[0]:  
                    time = row[0].split('\t')[1].split()[1]
                    timeList.append(time)

    time_difference(timeList, output_directory)
    writeFile(timeList, output_directory, "time_differences.txt")
    writeTimeListToFile(timeList, output_directory, "time_list.txt")

def writeTimeListToFile(timeList, output_directory, output_file):
    output_path = output_directory + "/" + output_file
    with open(output_path, 'w') as f:
        for time in timeList:
            f.write(time + '\n')

def writeFile(arr, output_directory, output_file):
    output_path = output_directory + "/" + output_file
    with open(output_path, 'w') as f:
        f.write("Time Differences:\n")
        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                time1 = time_to_seconds(arr[i])
                time2 = time_to_seconds(arr[i+1])
                difference_seconds = time2 - time1
                difference_time = format_time_difference(difference_seconds)
                f.write(f"Time {i//2 + 1}: {difference_time}\n")
            else:
                time_str = arr[i]
                hours, minutes, seconds = map(int, time_str.split(':'))
                seconds_total = hours * 3600 + minutes * 60 + seconds
                difference_time = format_time_difference(seconds_total)
                f.write(f"Time {i//2 + 1}: {difference_time}\n")

def time_difference(arr, output_directory):
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            time1 = time_to_seconds(arr[i])
            time2 = time_to_seconds(arr[i+1])
            difference_seconds = time2 - time1
            difference_time = seconds_to_time(difference_seconds)
            print(f"Time {i//2 + 1}: {format_time_difference(difference_seconds)}")

        else:
            time_str = arr[i]
            hours, minutes, seconds = map(int, time_str.split(':'))
            seconds_total = hours * 3600 + minutes * 60 + seconds
            print(f"Time {i//2 + 1}: {format_time_difference(seconds_total)}")

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def format_time_difference(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_difference_str = ""
    if hours > 0:
        time_difference_str += f"{hours} hour"
        if hours > 1:
            time_difference_str += "s"
        if minutes > 0 or seconds > 0:
            time_difference_str += ", "
    if minutes > 0:
        time_difference_str += f"{minutes} minute"
        if minutes > 1:
            time_difference_str += "s"
        if seconds > 0:
            time_difference_str += " and "
    if seconds > 0:
        time_difference_str += f"{seconds} second"
        if seconds > 1:
            time_difference_str += "s"
    return time_difference_str

def browse_output_directory():
    output_directory = filedialog.askdirectory(initialdir="/", title="Select directory")
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory)

def browse_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def search():
    file_path = file_entry.get()
    searchKey = search_entry.get()
    dateKey = date_entry.get()
    output_directory = output_directory_entry.get()
    print_csv_with_index(file_path, searchKey, dateKey, output_directory)

# Tkinter setup
root = tk.Tk()
root.title("Attendance")
root.minsize(500, 200)  # Set minimum width and height of the window
root.maxsize(500, 200) 

# File Selection
file_label = tk.Label(root, text="CSV File:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Output Directory Selection
output_directory_label = tk.Label(root, text="Output Directory:")
output_directory_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
output_directory_entry = tk.Entry(root, width=50)
output_directory_entry.grid(row=1, column=1, padx=5, pady=5)
browse_output_button = tk.Button(root, text="Browse", command=browse_output_directory)
browse_output_button.grid(row=1, column=2, padx=5, pady=5)

# Search
search_label = tk.Label(root, text="Search Key:")
search_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
search_entry = tk.Entry(root)
search_entry.grid(row=2, column=1, padx=5, pady=5)

# Date
date_label = tk.Label(root, text="Date (optional):")
date_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
