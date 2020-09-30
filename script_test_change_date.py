import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '120'
name_file = 'change_date_example.mp4'

def changeDate(data):
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

    #pegar tela e definir data
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Definir data')

    #pegar tela e definir data
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects(data)
    time.sleep(2)

    obj.get_objects('OK')

    #pegar tela e desabilitar data e hora automaticas
    time.sleep(2)
    dev.get_screen(device)
    obj.get_objects('Data e hora automáticas')

    time.sleep(2)
    events.event_home()
    screen.get_record(device)
    events.reboot()

