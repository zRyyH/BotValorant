import keyboard

class KeyboardMonitor:
    def __init__(self, main):
        self.main = main
        self.hook_keyboard()

    def hook_keyboard(self):
        keyboard.hook(self.on_key_event)

    def on_key_event(self, event):
        match event.name:
            case '=':
                self.main.farmRunning = True
                
            case '-':
                self.main.farmRunning = False

            case '/':
                self.main.counter_matchs = 2

            case '*':
                self.main.counter_matchs = 1

            case '+':
                self.main.counter_matchs = 0

    def stop_monitoring(self):
        keyboard.unhook_all()
        exit()