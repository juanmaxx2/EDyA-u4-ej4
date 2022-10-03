class Nodo:
    __frecuencia = None
    __izq = None
    __der = None
    __car = None

    def __init__(self, item, car):
        self.__frecuencia = item
        self.__car = car
        self.__izq = None
        self.__der = None
        
    def setItem(self, x):
        self.__frecuencia = x
    
    def setIzq(self,izq):
        self.__izq = izq
    
    def setDer(self, der):
        self.__der = der
    
    def setCar(self, car):
        self.__car = car
    
    def getItem(self):
        return self.__frecuencia
    
    def getIzq(self):
        return self.__izq
    
    def getDer(self):
        return self.__der

    def getCar(self):
        return self.__car

    def __eq__(self, texto):
        if type(texto) == str:
            return self.__car == texto
        
    def __gt__(self, item):
        if type(item) == Nodo:
            return self.__frecuencia < item.getItem()