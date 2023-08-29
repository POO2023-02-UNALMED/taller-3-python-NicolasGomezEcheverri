class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volume = 1
        self._precio = 500
    
    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        self._canal = canal
    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volume):
        self._volume = volume
    def getVolumen(self):
        return self._volume
    
    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == True and self._canal < 120:
            self._canal += 1
    def canalDown(self):
        if self._estado == True and self._canal > 1:
            self._canal -= 1
    
    def volumenUp(self):
        if self._estado == True and self._volume < 7:
            self._volume += 1
    def volumenDown(self):
        if self._estado == True and self._volume > 0:
            self._volume -= 1