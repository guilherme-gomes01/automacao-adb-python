import subprocess
import time

def record_screen():
    print("GRAVANDO TELA")
    output = subprocess.Popen("adb shell screenrecord --time-limit 30 /sdcard/DCIM/example.mp4", shell=True, stdout=subprocess.PIPE)

def print_screen():
    print("Tirando print da tela")
    output = subprocess.Popen("adb shell screencap -p /sdcard/DCIM/screenshot.png", shell=True, stdout=subprocess.PIPE)

def get_record(serial):
    time.sleep(3)
    print("PASSANDO ARQUIVO GRAVADO PARA COMPUTADOR")
    output = subprocess.Popen('adb -s %s pull /sdcard/DCIM/date_and_hour.mp4'%serial, shell=True, stdout=subprocess.PIPE)

def record_screen(limit, name):
    print("GRAVANDO TELA")
    output = subprocess.Popen("adb shell screenrecord --time-limit %s /sdcard/DCIM/%s"%(limit, name), shell=True, stdout=subprocess.PIPE)

