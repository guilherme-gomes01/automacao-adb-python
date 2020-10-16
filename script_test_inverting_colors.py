'''
    Algoritmo script_test_inverting_colors.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo automatiza uma série de comandos adb (android debug bridge) que realizam em um device (os testes foram
               realizados em um emulador android pixel 3 com Android 9) a operação de inversão de cores.

    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import subprocess
import time
import script_device_functions as dev
import script_events as events
import script_screen_functions as screen
import script_object_functions as obj

time_limit = '10'
name_file = 'inverting_colors_example.mp4'


def enable_disable_colors():
    print("ENABLES")
    subprocess.Popen('adb shell settings put secure accessibility_display_inversion_enabled 1', shell=True, stdout=subprocess.PIPE)
    time.sleep(2)
    events.swipe_screen()
    time.sleep(2)
    print("DISABLES")
    subprocess.Popen('adb shell settings put secure accessibility_display_inversion_enabled 0', shell=True, stdout=subprocess.PIPE)
    time.sleep(3)


def inverting_colors():
    screen.record_screen(time_limit, name_file)
    device = dev.get_devices()
    enable_disable_colors()
    events.event_back()
    screen.get_record(device, name_file)
