import os
import time
import script_test_open_app as openApp
import script_test_search as search
import script_test_change_language as cLanguage
#import script_test_transfer_files as tFiles
import script_test_change_date as mudaData
import script_test_change_hour as mudaHora
#import script_test_install_uninstall as installUnistall
#import script_test_inverting_colors as colors
#import script_test_screen_rotation as sRotation



print("Escolha a opção:\n\t1 - app\n\t2 - Pesquisa\n\t3 - Mudar linguagem")

app = input("Digite o nome do aplicativo: ")
openApp.openApp(app)

os.system('cls')  # For Windows
os.system('clear')  # For Linux/OS X
time.sleep(2)
pesq = input("Digite os termos da pesquisa (substitua o espaço por '%'): ")
search.pesquisa(pesq)

'''
cLanguage.change_language()

dt = input("Digite a data: ")
mudaData.changeDate(dt)
'''