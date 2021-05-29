import pyautogui
import time
from datetime import datetime

def enter_meet_id():
    meetingID = pyautogui.prompt(text='Enter your meeting ID', title='Meeting ID', default='')
    time.sleep(1)
    pyautogui.press('win', interval=0.5)
    time.sleep(1)
    pyautogui.typewrite('chrome', interval=0.5)
    time.sleep(1)
    pyautogui.press('enter', interval=0.5)
    time.sleep(13)
    pyautogui.typewrite('https://'+ meetingID, interval=0.3)
    # time.sleep(1)
    time.sleep(1)
    pyautogui.press('enter', interval=0.5)

def mic_camera_off():
    # pyautogui.hotkey('ctrl', 'd')  # Press the Ctrl-D hotkey combination to mute mic.
    pyautogui.hotkey('ctrl', 'e')    # Press the Ctrl-E hotkey combination to mute camera.

def join_meet():
    pyautogui.click(1342, 660)  # Move the mouse to XY coordinates and click the join button.

def end_meet():
    pyautogui.click(961, 1020)  # Move the mouse to XY coordinates and click the end call.

def present_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M %p", t)    
    return current_time

class monday:
    def automata(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time
        # print(custom_time)

    def OS(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def COA(self):
        date_string = '11:23 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def Humanity(self):
        date_string = '12:35 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OS2(self):
        date_string = '02:02 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

class tuesday:
    def automata(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time
        # print(custom_time)

    def COA(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OS(self):
        date_string = '11:23 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def Maths(self):
        date_string = '12:35 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def IT_workshop(self):
        date_string = '02:02 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

class wednesday:
    def Constitution(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time
        # print(custom_time)

    def SPL(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OS(self):
        date_string = '11:23 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def Maths(self):
        date_string = '12:35 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

class thursday:
    def Constitution(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time
        # print(custom_time)

    def SPL(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OB(self):
        date_string = '11:23 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def Humanity(self):
        date_string = '12:35 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

class friday:
    def OS(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time
        # print(custom_time)

    def OB(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OS_lab(self):
        date_string = '12:35 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def SPL(self):
        date_string = '02:02 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

class saturday:
    def Automata(self):
        date_string = '9:00 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def OB(self):
        date_string = '10:15 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def COA(self):
        date_string = '11:23 AM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

    def SPL(self):
        date_string = '02:02 PM'
        format = '%H:%M %p'
        my_date = datetime.strptime(date_string, format)
        custom_time = my_date.strftime(format)
        return custom_time

if __name__ == "__main__":

    m = monday()
    print("-Monday time")
    print(" Automata Time "+ m.automata())
    print(" OS Time "+ m.OS())
    print(" COA Time "+ m.COA())
    print(" Humanity Time "+ m.Humanity())
    print(" OS2 Time "+ m.OS2())

    print("\n");

    t = tuesday()
    print("-Tuesday time")
    print(" Automata Time "+ t.automata())
    print(" COA Time "+ t.COA())
    print(" OS Time "+ t.OS())
    print(" Maths Time "+ t.Maths())
    print(" OS2 Time "+ t.IT_workshop())

    print("\n");
    
    w = wednesday()
    print("-Wednesday time")
    print(" Constitution Time "+ w.Constitution())
    print(" SPL Time "+ w.SPL())
    print(" OS Time "+ w.OS())
    print(" Maths Time "+ w.Maths())

    print("\n");
    
    th = thursday()
    print("-Thursday time")
    print(" Constitution Time "+ th.Constitution())
    print(" SPL Time "+ th.SPL())
    print(" OB Time "+ th.OB())
    print(" Humanity Time "+ th.Humanity())

    print("\n");

    f = friday()
    print("-Friday time")
    print(" OS Time "+ f.OS())
    print(" OB Time "+ f.OB())
    print(" OS Lab Time "+ f.OS_lab())
    print(" SPL Time "+ f.SPL())

    print("\n");

    s = saturday()
    print("-Saturday time")
    print(" Automata Time "+ s.Automata())
    print(" OB Time "+ s.OB())
    print(" COA Time "+ s.COA())
    print(" SPL Time "+ s.SPL())

    print("\n")

    print("Present Time "+present_time()) 