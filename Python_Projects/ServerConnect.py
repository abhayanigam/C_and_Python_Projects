# pip install paramiko
import paramiko
import os

def connectToPrint(serverIp, private_key_path, username, log_file_path):
    private_key = paramiko.RSAKey(filename=private_key_path)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(serverIp, username=username, pkey=private_key)

    try:
        try:
            printSelection = input("Enter 't' for 'tail' / 'tn' for 'tail -n' / 's' for 'sudo' :")
            if printSelection == 't':
                command = 'tail -f ' + log_file_path
            elif printSelection == 'tn':
                command = 'tail -n 150 ' + log_file_path
            elif printSelection == 's':
                command = 'sudo vi ' + log_file_path
            
            stdin, stdout, stderr = ssh.exec_command(command)

        except KeyboardInterrupt:
            print("\nUser interrupted. Wrong Choice")
            ssh.close()
        
        for line in stdout:
            print(line.strip())

    except KeyboardInterrupt:
        print("\nUser interrupted. Closing the connection.")
        ssh.close()

def setupConnection():
    server_options = {
        "1": "3.6.72.223",
        "2": "3.7.98.232"
    }

    print("Select a server:")
    for key, value in server_options.items():
        print(f"{key}. {value}")

    server_choice = input("Enter the number corresponding to your choice: ")
    
    if server_choice not in server_options:
        print("Invalid choice. Program will exit.")
        exit()

    serverIp = server_options[server_choice]
    private_key_filename = "1team-non-prod.pem"
    private_key_path = os.path.join("/home/1team009/DevEnv", private_key_filename)
    username = "ubuntu"

    if server_choice == "1":
        log_file_options = {
            "1": "logs/sarah/sarah-console.log",
            "2": "logs/frodo/frodo-console.log",
            "3": "logs/1team-subscriber/1team-subscriber-console.log"
        }
    elif server_choice == "2":
        log_file_options = {
            "1": "logs/wot-subscriber-console.log",
            "2": "logs/wot-utilities-console.log"
        }
    else:
        print("Invalid server choice. Program will exit.")
        exit()

    print("Select a log file:")
    for key, value in log_file_options.items():
        print(f"{key}. {value}")

    log_file_choice = input("Enter the number corresponding to your choice: ")

    if log_file_choice not in log_file_options:
        print("Invalid choice. Program will exit.")
        exit()

    log_file_path = log_file_options[log_file_choice]

    return serverIp, private_key_path, username, log_file_path

if __name__ == "__main__":
    serverIp, private_key_path, username, log_file_path = setupConnection()
    connectToPrint(serverIp, private_key_path, username, log_file_path)

    reConnect = input("Type 'y' to reconnect, 'n' to close: ")

    while reConnect.lower() == 'y':
        serverIp, private_key_path, username, log_file_path = setupConnection()
        connectToPrint(serverIp, private_key_path, username, log_file_path)
        reConnect = input("Connect One More Time ==> type 'y' to reconnect, 'n' to close: ")
    
    print("Program closed.")