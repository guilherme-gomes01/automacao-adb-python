'''
    Algoritmo script_test_open_app.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de abertura de um determinado app.
    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

''' variáveis que definem tempo limite e nome da gravação'''
time_limit = '10'
name_file = 'open_app_example.mp4'

def openApp(name_app):
    device = dev.get_devices()
    screen.record_screen(time_limit, name_file)
    events.swipe_screen()
    dev.get_screen(device)
    obj.get_objects(name_app)
    time.sleep(5)
    events.event_home()
    screen.get_record(device, name_file)
