import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import tkinter as tk
from tkinter import filedialog
import csv

# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 

# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 

app = ctk.CTk()  
app.minsize(500, 600) 
app.maxsize(500, 600) 
app.title("Check Attendance") 

dark_mode = True

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

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
            # print(f"Time {i//2 + 1}: {format_time_difference(difference_seconds)}")

        else:
            time_str = arr[i]
            hours, minutes, seconds = map(int, time_str.split(':'))
            seconds_total = hours * 3600 + minutes * 60 + seconds
            # print(f"Time {i//2 + 1}: {format_time_difference(seconds_total)}")

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


frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

# Toggle Switch
switch_var = ctk.StringVar(value="on")

def switch_event():
    toggle_theme()

switch_1 = ctk.CTkSwitch(master=frame, command=switch_event,
                          variable=switch_var, onvalue="on", offvalue="off", text="Mode")
switch_1.pack(anchor="ne", padx=10, pady=10)

label = ctk.CTkLabel(master=frame,text='Enter The Details', font=('Helvetica', 20)) 
label.pack(pady=12,padx=10) 

file_entry = ctk.CTkEntry(master=frame,placeholder_text="Destination", height =40, width = 350)
file_entry.pack(pady=12,padx=10) 
browse_button = ctk.CTkButton(master=frame,text='Browse File',command=browse_file ,height =40, width =350) 
browse_button.pack(pady=12,padx=10) 

output_directory_entry = ctk.CTkEntry(master=frame,placeholder_text="Destination To Save The File", height =40, width = 350)
output_directory_entry.pack(pady=12,padx=10) 
browse_buttonbrowse_output_button = ctk.CTkButton(master=frame,text='Browse To Save The File',command=browse_output_directory,height =40, width = 350) 
browse_buttonbrowse_output_button.pack(pady=12,padx=10) 

search_entry= ctk.CTkEntry(master=frame,placeholder_text="Search Key:", height =40, width = 350) 
search_entry.pack(pady=12,padx=10) 

date_entry= ctk.CTkEntry(master=frame,placeholder_text="Date (optional)", height =40, width = 350) 
date_entry.pack(pady=12,padx=10) 

button = ctk.CTkButton(master=frame,text='Search',command=search ,height =40, width = 350) 
button.pack(pady=12,padx=10)  


app.mainloop()
