'''
    Algoritmo main.py
    Autores: Diego Torres, Giovanna S. Teodoro e João Guilherme S. Gomes
    Descrição: O algoritmo agrega todas as funções criadas para automatizar comandos adb, com interface para escolha
               das funcionalidades.
    OBS: A descrição completa do código encontra-se em bit.ly/hefesto7-doc
'''

import os
import time
import script_test_open_app as openApp
import script_test_search as search
import script_test_change_language as cLanguage
import script_test_transfer_files as tFiles
import script_test_change_date as mudaData
import script_test_change_hour as mudaHora
import script_test_install_uninstall as IU
import script_test_inverting_colors as colors
import script_test_screen_rotation as sRotation


def menu(opcao):
    if opcao == 1:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        app = input("Digite o nome do aplicativo: ")
        openApp.openApp(app)

    elif opcao == 2:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        pesq = input("Digite os termos da pesquisa (substitua o espaço por '%'): ")
        search.test_search(pesq)

    elif opcao == 3:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        cLanguage.change_language()

    elif opcao == 4:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        tFiles.transfer_files()

    elif opcao == 5:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        dt = input("Digite a data: ")
        mudaData.changeDate(dt)

    elif opcao == 6:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        hr = input("Digite a hora: ")
        min = input("Digite o minuto: ")
        mudaHora.changeHour(hr, min)

    elif opcao == 7:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        IU.install_uninstall()

    elif opcao == 8:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        colors.inverting_colors()

    elif opcao == 9:
        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X
        sRotation.rotation()

    else:
        print("Opção inválida")


def main():
    resposta = 's'

    while resposta == 's':
        print("-----------------------------------------------------"
              "\nEscolha a opção:\n\t1 - Open app\n\t2 - Search\n\t3 - Change language\n\t4 - Transfer files"
              "\n\t5 - Change date\n\t6 - Change hour\n\t7 - Install and Uninstall\n\t8 - Inverting colors\n\t9 - Screen rotation"
              "\n-----------------------------------------------------")
        op = int(input("Digite a opção: "))
        menu(op)

        os.system('cls')  # For Windows
        os.system('clear')  # For Linux/OS X

        resposta = input("\nDeseja continuar (s/n)? ")
        if resposta == 'n':
            break

#------ EXECUÇÃO DO MENU ------
main()

