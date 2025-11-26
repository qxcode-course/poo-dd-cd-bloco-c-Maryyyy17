class Client:
    def __init__(self, name : str) : 
        self.__name = name

    def __toString__(self) :
        return f"{self.__name}"
    
    def getName(self) :
        return self.__name
    
class Market :
    def __init__ (self, caixas : int) :
        self.__caixas : list[Client|None] = []
        for i in range(caixas) :
            self.__caixas.append(None)
        self.__fila : list[Client] = []
    
    def __str__ (self) :
        caixas = ",".join(["-----" if a == None else str(a) for a in self.__caixas])
        fila = ",".join([str(a) for a in self.__fila])
        return f"Caixas: [{caixas}]/nEspera: [{fila}]"
    
    def arrive (self, pessoa: Client) :
        person = pessoa
        self.__fila.append(person)

    def call(self, index : int) :
        if self.__fila == [] :
            print("fail: sem clientes")
            return
        if self.__caixas[index] != None:
            print("fail: caixa ocupado")
            return
        self.__caixas[index] = self.__fila[0]
        del self.__fila[0]

    def finish (self, index : int) :
        if index < 0 or index >= len(self.__caixas) :
            print("fail: caixa inexistente")
            return
        if self.__caixas[index] == None :
            print("fail : caixa vazio")
            return
        self.__caixas[index] = None

def main() :
    mercado = Market (0)

    while True :
        line = input()
        args : list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end" :
            break
        elif args[0] == "show" :
            print(mercado)
        elif args[0] == "init" :
            mercado.arrive(pessoa)
        elif args[0] == "call" :
            fila = int(args[1])
            mercado.call(fila)
        elif args[0] == "finish" :
            finalizar = int(args[1])
            mercado.finish(finalizar)
        else :
            print("fail: comando inválido")



    
