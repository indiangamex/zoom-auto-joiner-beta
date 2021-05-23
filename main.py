import subprocess
import pyautogui
import keyboard
import time

def zoom_auto_join(id, password):
    subprocess.run("\"Zoom.lnk\"",
                   shell = True,
                   cwd = "C:\\Users\\ghosh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom")

    while True:
        join = pyautogui.locateOnScreen("assets\\join.png")
        if join != None:
            pyautogui.click(join)
            print("initiated !")
            time.sleep(1)
            keyboard.write(id)
            break
        else:
            print("initiating !!!")
            continue
    while True:
        video_off = pyautogui.locateOnScreen("assets\\video_off.png")
        if video_off != None:
            pyautogui.click(video_off)
            print("turned of video !")
            break
        else:
            print("not yet turned of video !")
            continue
    while True:
        join_2 = pyautogui.locateOnScreen("assets\\join_2.png")
        if join_2 != None:
            pyautogui.click(join_2)
            time.sleep(3)
            keyboard.write(password)
            keyboard.press_and_release("enter")
            print("we made it to the class room !")
            break
        else:
            print("not clicked")
            continue

zoom_auto_join("8587659513", "prateeksir123")
