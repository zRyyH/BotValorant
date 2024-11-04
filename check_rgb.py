from recorder import Recorder

class CheckRGB():
    def __init__(self):
        self.recorder = Recorder()
        self.coords = {
            'saguao': [(27, 199, [225, 232, 236])],
            'lobby_ranked': [(100, 430, [174, 232, 30])],
            'killjoy': [(669, 149, [49, 223, 247])],
            'fps_grafic': [(232, 1763, [255, 255, 255])],
            'purchase_phase': [(253, 930, [255, 255, 255])],
            'lobby_jogar': [(5, 940, [70, 57, 216])],
            'unranked': [(827, 932, [255, 255, 255])],
            'ferro': [(815, 933, [116, 118, 116])],
            'gamepass': [(22, 1832, [206, 215, 221])],
            'alert': [(540, 610, [40, 35, 30]), (540, 1310, [40, 35, 30])],
            'gamepass_banner': [(86, 666, [85, 70, 255]), (394, 818, [225, 232, 236])]
        }
        
    def compare(self, data, margin = 1):
        for y, x, expected in data:
            if not all(abs(a - b) <= margin for a, b in zip(self.recorder.capture()[y][x], expected)):
                return False
        return True
    
    def check(self):
        ids = {}
        for id in self.coords.keys():
            ids.update({id: self.compare(data=self.coords[id])})
        return ids