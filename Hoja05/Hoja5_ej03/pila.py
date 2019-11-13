import disco

class Pila:
    
    def __init__(self, tamano, nombre):
        self.nombre = nombre;
        self.pointer = -1
        self.pila = []
        for i in range(tamano):
            self.pila.append(0)

    def checkIndex(self):
        return self.pointer >=-1 and self.pointer<len(self.pila)

    def checkOrden(self, discon):
        if self.pointer >=0:
            return discon.getLongitud()-1<self.pila[self.pointer].getLongitud()

    def getPila(self):
        return self.pila
    
    def getNombre(self):
        return self.nombre
    
    def getPointer(self):
        return self.pointer

    def push(self, discon):
        if self.checkIndex() and self.checkOrden(discon) or self.isEmpty():
            self.pointer+=1
            self.pila[self.pointer] = discon
            return True
        else:
            #print('No se puede relizar el push')
            return False
            
    def pop(self):
        if self.isEmpty() == False and self.checkIndex():
            self.pointer-=1
        #else:
            #print('No se puede realizar el pop')

    def isEmpty(self):
        if self.pointer == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if self.pointer == len(self.pila)-1:
            return True
        else:
            return False

    def peek(self):
        return self.pila[self.pointer]
