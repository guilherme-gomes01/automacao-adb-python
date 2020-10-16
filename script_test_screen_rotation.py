'''
    Algoritmo script_test_screen_rotation.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de rotação de tela.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '20'
name_file = 'screen_rotation_example.mp4'


def screen_rotation(serial):
    print("TURNING OFF AUTOMATIC SCREEN ROTATION")
    output = subprocess.Popen(
        'adb -s %s shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0' % serial,
        shell=True, stdout=subprocess.PIPE).communicate()[0]
    print("LANDSCAPE MODE")
    output = subprocess.Popen(
        'adb -s %s shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:1' % serial,
        shell=True, stdout=subprocess.PIPE).communicate()[0]
    time.sleep(3)
    print("PORTRAIT MODE")
    output = subprocess.Popen(
        'adb -s %s shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0' % serial,
        shell=True, stdout=subprocess.PIPE).communicate()[0]
    time.sleep(3)
    events.event_home()
    time.sleep(3)

def rotation():
    screen.record_screen(time_limit, name_file)
    device = dev.get_devices()
    dev.get_screen(device)
    obj.get_objects('Telefone')
    screen_rotation(device)
    screen.get_record(device, name_file)
