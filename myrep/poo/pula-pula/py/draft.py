class Kid :
    def __init__(self, name: str, age: int) :
        self.__name: str = name
        self.__age: int = age

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"
    
    def getName(self) :
        return self.__name
    
    def getAge(self) :
        return self.__age
    
    def setName(self, nome: str):
        self.__name = nome

    def setAge(self, idade: int):
        self.__age = idade

class Trampoline :
    def __init__(self) :
        self.__Playing : list[Kid] = []
        self.__Waiting : list[Kid] = []

    def __str__(self) -> str:
        espera = ", ".join(map(str,self.__Waiting))
        brincar = ", ".join(map(str,self.__Playing))
        return f"[{espera}] => [{brincar}]"
    
    def getPlaying(self):
        return self.__Playing
    
    def getWaiting(self):
        return self.__Waiting
    
    def removeFromList(self, nome: str, cria :list[Kid]) -> Kid|None:
        for i in cria :
            if i.getName == nome :
                cria.remove(i)
                return i
            else:
                return None
            
    def arrive(self,cria : Kid) :
        self.getWaiting().append(cria)

    def enter(self) :
        espera = self.getWaiting()
        if not espera :
            return
        pirralho = espera.pop()
        self.getPlaying().append(pirralho)

    def remove(self, name : str) -> Kid|None:
        menino = self.removeFromList(name,self.getPlaying())
        if menino is not None:
            return menino
        menina = self.removeFromList(name, self.getWaiting())
        if menina is not None:
            return menina
        print(f"fail:{name} nao está no pula pula")
        return None
    
def main() :
    pula = Trampoline()
    while True :
        line = input()
        args = line.split(" ")
        print("$" + line)
       
        if args[0] == "end" :
            break
        elif args[0] == "arrive" :
            nome = args[1]
            idade = int(args[2])
            k = Kid(nome, idade)   
            pula.arrive(k)
        elif args[0] == "show" :
            print(pula)
        elif args[0] == "enter" :
            pula.enter
        elif args[0] == "leave" :
            pula.removeFromList
        elif args[0] == "remove" :
            pessoa = args[1]
            pula.remove(pessoa)
main()