'''
    Algoritmo script_test_change_language.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de alteração de linguagem do dispositivo.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '30'
name_file = 'change_language_example.mp4'

def change_language():
    #pegar o dispositivo e gravar a tela
    device = dev.get_devices()
    screen.record_screen(time_limit, name_file)

    #pegar tela e abrir configurações
    events.swipe_screen()
    dev.get_screen(device)
    obj.get_objects('Configurar')

    #pegar tela e abrir sistema
    time.sleep(3)
    events.swipe_screen()
    dev.get_screen(device)
    obj.get_objects('Sistema')

    #pegar tela e abrir idiomas e entrada
    time.sleep(3)
    dev.get_screen(device)
    obj.get_objects('Idiomas e entrada')

    #pegar tela e abrir Idiomas
    time.sleep(3)
    dev.get_screen(device)
    obj.get_objects('Idiomas')

    time.sleep(3)
    #dev.get_screen(device)

    output = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)
    time.sleep(3)
    output1 = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)
    time.sleep(3)
    events.event_home()