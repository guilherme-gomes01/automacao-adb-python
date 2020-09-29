import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

#pegar o dispositivo e gravar a tela
device = dev.get_devices()
screen.record_screen()

#pegar tela e abrir configurações
events.swipe_screen()
dev.get_screen(device)
obj.get_objects('Configurar')

#pegar tela e abrir sistema
time.sleep(2)
events.swipe_screen()
dev.get_screen(device)
obj.get_objects('Sistema')

#pegar tela e abrir idiomas e entrada
time.sleep(2)
dev.get_screen(device)
obj.get_objects('Idiomas e entrada')

#pegar tela e abrir Idiomas
time.sleep(3)
dev.get_screen(device)
obj.get_objects('Idiomas')

time.sleep(3)
dev.get_screen(device)

output = subprocess.Popen("adb shell input swipe 926 242 926 440 500", shell=True, stdout=subprocess.PIPE)
time.sleep(2)
output = subprocess.Popen("adb shell input swipe 926 242 926 440 500", shell=True, stdout=subprocess.PIPE)