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
    time.sleep(1)
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

def operation():
    enter_meet_id()
    time.sleep(5)
    mic_camera_off()
    time.sleep(3)
    join_meet()
    time.sleep(1)

if __name__ == "__main__":

    m = monday()
    t = tuesday()
    w = wednesday()
    th = thursday()
    f = friday()
    s = saturday()

    print("Present Time is "+present_time()) 

    date_string = '15:31 PM'
    format = '%H:%M %p'
    end_date = datetime.strptime(date_string, format)
    end_time = end_date.strftime(format)

    while(True):
        if(m.automata() == present_time()):
            operation()

        if(m.OS() == present_time()):
            end_meet()
            operation()

        if(m.COA() == present_time()):
            end_meet()
            operation()

        if(m.Humanity() == present_time()):
            end_meet()
            operation()

        if(m.OS2() == present_time()):
            end_meet()
            operation()

#-----------------------------------------------
        if(t.automata() == present_time()):
            operation()

        if(t.COA() == present_time()):
            end_meet()
            operation()

        if(t.OS() == present_time()):
            end_meet()
            operation()

        if(t.Maths() == present_time()):
            end_meet()
            operation()

        if(t.IT_workshop() == present_time()):
            end_meet()
            operation()

#-----------------------------------------------
        if(w.Constitution() == present_time()):
            operation()

        if(w.SPL() == present_time()):
            end_meet()
            operation()

        if(w.OS() == present_time()):
            end_meet()
            operation()

        if(w.Maths() == present_time()):
            end_meet()
            operation()

#-----------------------------------------------
        if(th.Constitution() == present_time()):
            operation()

        if(th.SPL() == present_time()):
            end_meet()
            operation()

        if(th.OB() == present_time()):
            end_meet()
            operation()

        if(th.Humanity() == present_time()):
            end_meet()
            operation()

#-----------------------------------------------
        if(f.OS() == present_time()):
            operation()

        if(f.OB() == present_time()):
            end_meet()
            operation()

        if(f.OS_lab() == present_time()):
            end_meet()
            operation()

        if(f.SPL() == present_time()):
            end_meet()
            operation()

#-----------------------------------------------
        if(s.Automata() == present_time()):
            operation()

        if(s.OB() == present_time()):
            end_meet()
            operation()

        if(s.COA() == present_time()):
            end_meet()
            operation()

        if(s.SPL() == present_time()):
            end_meet()
            operation()

        if(end_time == present_time()):
            end_meet()
            break

        print("Enjoy There is no class........!")
        break;