import csv

def extract_times(file_path, searchKey, dateKey=None):
    timeList = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, row in enumerate(csv_reader):
            if searchKey in row[0]:
                if dateKey is None or dateKey in row[0]:
                    time = row[0].split('\t')[1].split()[1]
                    timeList.append(time)
    return timeList

def print_csv_with_index(file_path, searchKey, dateKey=None):
    timeList = extract_times(file_path, searchKey, dateKey)
    print("\nYou've Searched For: " + searchKey)

    time_difference(timeList)
    writeTimeListToFile(timeList, "time_list.txt")

def writeTimeListToFile(timeList, output_file):
    output_path = r"C:\Users\abhay\Desktop\GitHubRepos\C_and_Python_Projects\Python_Projects\AttendanceCheckerCSV\\" + output_file
    with open(output_path, 'w') as f:
        for time in timeList:
            f.write(time + '\n')

def writeFile(content, output_file):
    output_path = r"C:\Users\abhay\Desktop\GitHubRepos\C_and_Python_Projects\Python_Projects\AttendanceCheckerCSV\\" + output_file
    with open(output_path, 'w') as f:
        f.write(content)

def time_difference(arr):
    differences = []
    total_seconds = 0
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):
            time1 = time_to_seconds(arr[i])
            time2 = time_to_seconds(arr[i+1])
            difference_seconds = time2 - time1
            total_seconds += difference_seconds
            differences.append(f"Time {i//2 + 1}: {format_time_difference(difference_seconds)}")
            print(differences[-1])
        else:
            time_str = arr[i]
            hours, minutes, seconds = map(int, time_str.split(':'))
            seconds_total = hours * 3600 + minutes * 60 + seconds
            total_seconds += seconds_total
            differences.append(f"Time {i//2 + 1}: {format_time_difference(seconds_total)}")
            print(differences[-1])
    
    total_time = seconds_to_time(total_seconds)
    differences.append(f"\nTotal Time: {format_time(total_time)}")
    print(differences[-1])

    content = "\n".join(differences)
    writeFile(content, "time_differences.txt")

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

def format_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return f"Time: {hours} hours, {minutes} minutes, {seconds} seconds"

def get_first_and_last_time(timeList):
    if timeList:
        first_time = timeList[0]
        last_time = timeList[-1]
        first_time_formatted = format_time(first_time)
        last_time_formatted = format_time(last_time)
        print(f"First time: {first_time_formatted}")
        print(f"Last time: {last_time_formatted}")
        content = f"First time: {first_time_formatted}\nLast time: {last_time_formatted}"
        writeFile(content, "first_and_last.txt")
    else:
        print("No times found.")

def main():
    file_path = r"C:\Users\abhay\Desktop\GitHubRepos\C_and_Python_Projects\Python_Projects\AttendanceCheckerCSV\1111_attlog.csv"  # Replace with the actual path to your CSV file

    searchKey = input("Enter the Number to search: ")
    dateKey = input("Enter the Date to search (optional, press enter to skip): ")

    while True:
        print("Select an option:")
        print("1. Search and print all details")
        print("2. Print first and last time only")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print_csv_with_index(file_path, searchKey, dateKey)
        elif choice == '2':
            timeList = extract_times(file_path, searchKey, dateKey)
            get_first_and_last_time(timeList)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()