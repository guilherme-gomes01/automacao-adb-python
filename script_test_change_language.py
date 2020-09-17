import subprocess
#import xml.etree.ElementTree as ET
import time
import script_test_search as teste1

device = teste1.get_devices()
teste1.record_screen()

#pegar tela e abrir configurações
teste1.swipe_screen()
teste1.get_screen(device)
teste1.get_apps('Configurar')

#pegar tela e abrir sistema
time.sleep(2)
teste1.swipe_screen()
teste1.get_screen(device)
teste1.get_apps('Sistema')

#pegar tela e abrir idiomas e entrada
time.sleep(2)
teste1.get_screen(device)
teste1.get_apps('Idiomas e entrada')

#pegar tela e alterar idioma
time.sleep(2)
teste1.get_screen(device)
teste1.get_apps('Idiomas')

time.sleep(2)
teste1.get_screen(device)

output = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)
time.sleep(2)
output = subprocess.Popen("adb shell input swipe 926 242 926 500 500", shell=True, stdout=subprocess.PIPE)