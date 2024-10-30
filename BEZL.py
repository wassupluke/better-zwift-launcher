import os, pyautogui, subprocess, time, win32gui, win32con

os.chdir("C:\\Users\\wassu\\AppData\\Roaming\\ZwiftHacks\\src")
subprocess.run(
        ["C:\\Program Files\\AutoHotkey\\AutoHotkey.exe", "zwift-login.ahk", "/launch"], 
        check=True, text=True
        )
while True:
    time.sleep(2)
    hwnd = win32gui.FindWindow(None, "Zwift")
    if hwnd != 0:
        break
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
