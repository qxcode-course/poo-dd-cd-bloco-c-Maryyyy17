class Client:
    def __init__(self, name : str) : 
        self.__name = name

    def __toString__(self) :
        return f"{self.__name}"
    
    def getName(self) :
        return self.__name
    
class Market :
    def __init__ (self, caixas : int) :
        self.__caixas = caixas
        self.__fila : Client|None = []
    
