class Control:
    def __init__(self):
        self._tv = None
    
    def enlazar(self, tv):
        self._tv = tv
    
    def turnOn(self):
        self._tv.turnOn()  
    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        if self._tv._canal < 120:
            self._tv.canalUp()
    def canalDown(self):
        if self._tv._canal > 1:
            self._tv.canalDown()
    
    def volumenUp(self):
        if self._tv._volume < 7:
            self._tv.volumenUp()
    def volumenDown(self):
        if self._tv._volume > 0:
            self._tv.volumenDown()
    
    def setCanal(self, canal):
        if canal <= 120 and canal >= 1:
            self._tv.setCanal(canal)
    
    def setVolumen(self, volume):
        if volume <= 7 and volume >= 0:
            self._tv.setVolumen(volume)
    
    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)
    
    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv