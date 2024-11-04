from autogui import AutoGUI
import time

class Actions():
    def __init__(self):
        self.AutoGUI = AutoGUI()
    
    def start_ranked(self):
        self.AutoGUI.click(930, 980)                   # Puxar partida ranqueada
        time.sleep(1.5)
        
    def close_alert(self):
        self.AutoGUI.press('esc')                      # Fechar alerta
        time.sleep(1.5)

    def select_killjoy(self):
        self.AutoGUI.click(185, 650)                   # Selecionar killjoy
        self.AutoGUI.click(950, 750)                   # Confirmar agente
        time.sleep(1.5)

    def place_turret(self):
        self.AutoGUI.press('s', interval=1)            # Andar para traz
        self.AutoGUI.press('e', interval=0.1)          # Ativar torreta
        time.sleep(1.5)
        self.AutoGUI.click(10, 10)                     # Colocar torreta
        time.sleep(1.5)

    def close_alert(self):
        self.AutoGUI.press('esc')                      # Fechar alerta
        time.sleep(1.5)

    def troll_mode(self):
        keys = ['s', 'a', 'd', 'space', '1', '2', 'y']
        self.AutoGUI.press_random(keys=keys)           # precionar tecla aleatoria por um periodo aleatorio
        time.sleep(1.5)
    
    def go_to_lobby(self):
        self.AutoGUI.click(930, 25)                    # Ir para saguao
        time.sleep(1.5)
    
    def go_to_ranked_mode(self):
        self.AutoGUI.click(430, 85)                    # Ir para o modo ranqueado
        time.sleep(1.5)
        
    def close_gamepass_banner(self):
        self.AutoGUI.click(960, 1000)                  # Fechar banner do gamepass
        time.sleep(1.5)
    