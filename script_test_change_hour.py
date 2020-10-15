'''
    Algoritmo script_test_change_hour.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de mudança de hora.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '120'
name_file = 'change_hour_example.mp4'

def changeHour(hora, minuto):
    #pegar o dispositivo e gravar a tela
    device = dev.get_devices()
    screen.record_screen(time_limit, name_file)

    #pegar tela e abrir configurações
    events.swipe_screen()
    dev.get_screen(device)
    obj.get_objects('Configurar')

    #pegar tela e abrir sistema
    time.sleep(2)
    events.swipe_screen()
    dev.get_screen(device)
    obj.get_objects('Sistema')

    #pegar tela e abrir Data e Hora
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Data e hora')

    #pegar tela e desabilitar data e hora automaticas
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Data e hora automáticas')

    #pegar tela e definir hora
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Definir hora')

    #pegar tela e definir hora
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects1(hora)
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects1(minuto)
    time.sleep(2)
    obj.get_objects('OK')

    #pegar tela e desabilitar data e hora automaticas
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Data e hora automáticas')

    time.sleep(2)
    events.event_home()
    #screen.get_record(device)
    events.reboot()

