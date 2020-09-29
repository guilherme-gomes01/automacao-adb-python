import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '40'
name_file = 'change_hour_example.mp4'


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
'''

#pegar tela e definir hora
time.sleep(3)
dev.get_screen(device)
obj.get_objects('3')
time.sleep(3)
obj.get_objects('55')
time.sleep(3)
obj.get_objects('OK')

screen.get_record(device)
'''

'''
output = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)
time.sleep(2)
output = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)
'''

