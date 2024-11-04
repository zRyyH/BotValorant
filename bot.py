from keyboard_monitor import KeyboardMonitor
from check_rgb import CheckRGB
from actions import Actions
from notify import notify

import traceback
import time


class Bot():
    def __init__(self):
        self.KeyboardMonitor = KeyboardMonitor(main=self)
        self.CheckRGB = CheckRGB()
        self.Actions = Actions()
        
        self.farmRunning = False
        self.counter_matchs = 0
    
    def execute_logic(self):
        try:
            state = self.CheckRGB.check()
            match state:
                case {'saguao': True, 'lobby_ranked': True, 'lobby_jogar': False, 'unranked': True, 'gamepass': True}:
                    self.counter_matchs = 2
                    self.Actions.start_ranked()
                    return 'START_UNRANKED'

                case {'saguao': True, 'lobby_ranked': True, 'lobby_jogar': False, 'ferro': True, 'gamepass': True}:
                    if self.counter_matchs > 0:
                        self.counter_matchs -= 1
                        self.Actions.start_ranked()
                        return 'START_FERRO'
                    else:
                        notify()
                        return 'READY_FERRO'
                
                case {'fps_grafic': True, 'purchase_phase': False}:
                    self.Actions.troll_mode()
                    return 'FPS_GRAFIC'

                case {'fps_grafic': True, 'purchase_phase': True}:
                    self.Actions.place_turret()
                    return 'PLACE_TURRET'
                    
                case {'killjoy': True}:
                    self.Actions.select_killjoy()
                    return 'SELECT_KILLJOY'

                case {'alert': True}:
                    self.Actions.close_alert()
                    return 'CLOSE_ALERT'

                case {'gamepass_banner': True}:
                    self.Actions.close_gamepass_banner()
                    return 'CLOSE_GAMEPASS_BANNER'

                case {'lobby_jogar': True}:
                    self.Actions.go_to_lobby()
                    return 'GO_TO_LOBBY'

                case {'lobby_jogar': False, 'saguao': True, 'lobby_ranked': False}:
                    self.Actions.go_to_ranked_mode()
                    return 'GO_TO_RANKED_MODE'
                
        except:
            traceback.print_exc()
            
        
    def startFarm(self):
        self.farmRunning = True
        
        while True:
            time.sleep(1)
            if self.farmRunning:
                state = self.execute_logic()
                print('|', state, self.farmRunning, self.counter_matchs)
                
obj = Bot()
obj.startFarm()