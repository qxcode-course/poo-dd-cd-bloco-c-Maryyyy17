class Lead :
    def __init__(self, hardness : str, thickness : float, size : int) :
        self.__hardness = hardness
        self.__thickness = thickness
        self.__size = size

    def __string__(self) :
        return f"<[{self.__hardness}:{self.__thickness:{self.__size}]}"
    
    def usagePerSheet(self) -> int :
        