import pyautogui
import time
import os
import tkinter as tk
from tkinter import messagebox

def abrir_erp_login():
    # ABERTURA DO SISTEMA
    print("Abrindo ERP")
    os.startfile('C:\\Program Files\\Alterdata\\ERP\\Bimer.exe')
    time.sleep(5)

    # INSERIR USUARIO
    pyautogui.doubleClick(950, 454)
    pyautogui.press('del')
    pyautogui.write('DEFIN')
    # time.sleep(1)

    # INSERIR DEFIN
    print("Inserindo Senha")
    pyautogui.click(919, 523)
    pyautogui.write('07082024')
    time.sleep(1)

    # ENTRAR
    print("Entrando")
    pyautogui.click(971, 647)
    time.sleep(3)

def extrair_relatorio_1():

    # EXPANDIR ESTOQUE
    pyautogui.click(121, 229)
    time.sleep(2)

    # ABRIR BI ESTOQUE
    pyautogui.click(101, 269)
    time.sleep(2)

    # RECUPERAR CENÁRIO 1
    pyautogui.click(145, 89)
    time.sleep(3)

    # SELECIONAR CENARIO 1
    pyautogui.doubleClick(990, 385)
    time.sleep(2)

    # FILTRAR 
    pyautogui.click(450, 86)
    time.sleep(30)

    # EXPORTAR
    print("Exportando")
    pyautogui.click(906, 84)
    time.sleep(1)

    # SELECIONANDO PARA SOBRESCREVER
    pyautogui.click(863, 305)
    time.sleep(1)

    # SALVAR
    print("Salvando")
    pyautogui.click(1252, 602)
    time.sleep(2)

    # CONFIRMAR SAVE
    pyautogui.click(915, 561)
    time.sleep(1)

    # ALTERNAR FILTRO E RESULTADO
    pyautogui.click(373, 81)
    time.sleep(5)

def extrair_relatorio_2():

    # RECUPERAR CENÁRIO 2
    pyautogui.click(150, 89)
    time.sleep(2)

    # SELECIONAR CENARIO 2
    pyautogui.doubleClick(977, 410)
    time.sleep(10)

    # FILTRAR 
    pyautogui.click(445, 91)
    time.sleep(60)

    # EXPORTAR
    print("Exportando")
    pyautogui.click(906, 84)
    time.sleep(1)

    # SELECIONANDO PARA SOBRESCREVER
    pyautogui.click(817, 326)
    time.sleep(1)

    # SALVAR
    print("Salvando")
    pyautogui.click(1252, 602)
    time.sleep(2)

    # CONFIRMAR SAVE
    pyautogui.click(915, 561)
    time.sleep(1)

    # ALTERNAR FILTRO E RESULTADO
    pyautogui.click(373, 81)
    time.sleep(10)

def extrair_relatorio_3():

    # RECUPERAR CENÁRIO 3
    pyautogui.click(150, 89)
    time.sleep(3)

    # SELECIONAR CENARIO 2
    pyautogui.doubleClick(791, 432)
    time.sleep(10)

    # FILTRAR 
    pyautogui.click(445, 91)
    time.sleep(60)

    # EXPORTAR
    print("Exportando")
    pyautogui.click(906, 84)
    time.sleep(1)

    # SELECIONANDO PARA SOBRESCREVER
    pyautogui.click(788, 345)
    time.sleep(1)

    # SALVAR
    print("Salvando")
    pyautogui.click(1252, 602)
    time.sleep(2)

    # CONFIRMAR SAVE
    pyautogui.click(915, 561)
    time.sleep(1)

def fechar_sistema():
    # FECHANDO SISTEMA
    pyautogui.click(1896, 12)
    time.sleep(1)

    # CONFIRMANDO
    pyautogui.click(832, 557)

def mostrar_pop_up_temporario():
    root = tk.Tk()
    root.title("Aviso")
    root.geometry("400x200+691+336")
    label = tk.Label(root, text="O programa está em execução.\nPor favor, não mexa no computador.", font=("Arial", 12))
    label.pack(expand=True, padx=20, pady=20)
    
    # Fechar a janela após 5 segundos
    root.after(5000, root.destroy)
    root.mainloop()

def main():
    mostrar_pop_up_temporario()
    abrir_erp_login()
    extrair_relatorio_1()
    extrair_relatorio_2()
    extrair_relatorio_3()
    fechar_sistema()
if __name__ == "__main__":
    main()

print("Finalizado")