import subprocess

def record_screen():
    print("GRAVANDO TELA")
    output = subprocess.Popen("adb shell screenrecord --time-limit 10 /sdcard/DCIM/example.mp4", shell=True, stdout=subprocess.PIPE)

def print_screen():
    print("Tirando print da tela")
    output = subprocess.Popen("adb shell screencap -p /sdcard/DCIM/screenshot.png", shell=True, stdout=subprocess.PIPE)
