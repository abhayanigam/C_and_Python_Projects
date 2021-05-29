import pyautogui #install --> pip install PyAutoGUI
import time

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

def show_everyone():
    pyautogui.click(1424, 162)  # Move the mouse to XY coordinates and click the show everyone.

def end_meet():
    pyautogui.click(961, 1020)  # Move the mouse to XY coordinates and click the end call.

if __name__ == "__main__":
    enter_meet_id()
    time.sleep(5)  # making a delay of 5 seconds

    mic_camera_off()

    time.sleep(3)  # making a delay of 3 seconds
    join_meet()

    time.sleep()
    show_everyone()

    time.sleep(25) #making a delay of 25 seconds
    end_meet()