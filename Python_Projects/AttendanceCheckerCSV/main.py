import csv

def print_csv_with_index(file_path, searchKey, dateKey=None):
    timeList = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            # if index >= 444:
            #     break
            if searchKey in row[0]:
                if dateKey is None or dateKey in row[0]:  
                    time = row[0].split('\t')[1].split()[1]
                    timeList.append(time)

    print(timeList)

    print("\nYou've Searched For: " + searchKey)

    time_difference(timeList)
    writeFile(timeList, "time_differences.txt")
    writeTimeListToFile(timeList, "time_list.txt")

def writeTimeListToFile(timeList, output_file):
    output_path = r"C:\Users\abhay\Desktop\CSVRead\\" + output_file
    with open(output_path, 'w') as f:
        for time in timeList:
            f.write(time + '\n')

def writeFile(arr, output_file):
    output_path = r"C:\Users\abhay\Desktop\CSVRead\\" + output_file
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


def time_difference(arr):
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

file_path = r"C:\Users\abhay\Desktop\CSVRead\1111_attlog.csv"  # Replace with the actual path to your CSV file

searchKey = str(input("Enter the Number to search : "))
dateKey = str(input("Enter the Date to search (optional, press enter to skip): "))

print_csv_with_index(file_path, searchKey, dateKey)