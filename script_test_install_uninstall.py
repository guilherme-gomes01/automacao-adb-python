'''
    Algoritmo script_test_install_uninstall.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de instalação e desinstalação de aplicativos.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '45'
name_file = 'install_uninstall_example.mp4'

def install_apps():
    print("INSTALANDO APKs")
    events.swipe_screen()
    time.sleep(2)
    output = subprocess.Popen("adb install ./apks/wikipedia.apk", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    output = subprocess.Popen("adb install ./apks/ankidroid.apk", shell=True, stdout=subprocess.PIPE)
    time.sleep(3)

def uninstall_apps():
    print("DESINSTALANDO APKs")
    events.swipe_screen()
    time.sleep(2)
    output = subprocess.Popen("adb uninstall org.wikipedia", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    output = subprocess.Popen("adb uninstall com.ichi2.anki", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    output = subprocess.Popen("adb shell input keyevent 4", shell=True, stdout=subprocess.PIPE)


def install_uninstall():
    device = dev.get_devices()
    screen.record_screen(time_limit, name_file)
    install_apps()
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Wikipédia')
    time.sleep(2)
    events.event_home()
    time.sleep(2)
    events.swipe_screen()
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('AnkiDroid')
    uninstall_apps()
    screen.get_record(device)



