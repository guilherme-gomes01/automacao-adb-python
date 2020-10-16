import subprocess
import time

'''
def record_screen():
    print("GRAVANDO TELA")
    output = subprocess.Popen("adb shell screenrecord --time-limit 30 /sdcard/DCIM/example.mp4", shell=True, stdout=subprocess.PIPE)
'''
def record_screen(limit, name):
    print("GRAVANDO TELA")
    output = subprocess.Popen("adb shell screenrecord --time-limit %s /sdcard/DCIM/%s"%(limit, name), shell=True, stdout=subprocess.PIPE)

def print_screen():
    print("Tirando print da tela")
    output = subprocess.Popen("adb shell screencap -p /sdcard/DCIM/screenshot.png", shell=True, stdout=subprocess.PIPE)

def get_record(serial, name):
    time.sleep(5)
    print("PULLING .mp4")
    output = subprocess.Popen('adb -s %s pull /sdcard/DCIM/%s'%(serial, name), shell=True, stdout=subprocess.PIPE)
