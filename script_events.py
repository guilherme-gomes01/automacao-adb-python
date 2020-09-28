import subprocess
import time

def event_home():
    print("Voltando a tela inicial")
    output = subprocess.Popen("adb shell input keyevent 3", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)

def event_back():
    print("Voltando a tela anterior")
    output = subprocess.Popen("adb shell input keyevent 4", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)

def tap_screen(app_name, x, y):
    print("Abrindo %s" % app_name)
    output = subprocess.Popen("adb shell input tap %s %s" % (x, y), shell=True, stdout=subprocess.PIPE)

def swipe_screen():
    output = subprocess.Popen("adb shell input swipe 300 2000 300 500 500", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)