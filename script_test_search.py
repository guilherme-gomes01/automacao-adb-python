'''
    Algoritmo script_test_search.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de pesquisa no Chrome.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj
import xml.etree.ElementTree as ET

time_limit = '20'
name_file = 'test_search_example.mp4'

device = dev.get_devices()

def search(search_text):
    dev.get_screen(device)
    time.sleep(2)
    obj.get_objects('Pesquisar ou digitar endereço da Web')
    time.sleep(2)
    output = subprocess.Popen("adb shell input text %s" %search_text, shell=True, stdout=subprocess.PIPE)
    time.sleep(1)
    output = subprocess.Popen("adb shell input keyevent 66", shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    events.swipe_screen()


def test_search(text_search):
    screen.record_screen(time_limit, name_file)
    dev.get_screen(device)
    #events.swipe_screen()
    obj.get_objects('Chrome')
    search(text_search)
    events.event_back()
    events.event_home()
    screen.get_record(device, name_file)

'''
def open_app():
    output = subprocess.Popen("adb shell monkey -p com.android.chrome 1", shell=True, stdout=subprocess.PIPE)
    text()
    
adb shell input touchscreen swipe 440 1615 440 1615 2000 (comando para simular um "long press")
'''
