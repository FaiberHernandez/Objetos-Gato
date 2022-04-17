class Gato:
    _especie = "mamifero"
    __estado = ""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__estado = "Despierto"
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            self._edad = 0
        else:
            self._edad = edad
        
    def maullar():
        print("meow")
    
    def comer(self):
        self.__estado = "Llenito"
    
    def jugar(self):
        self.__estado = "Cansado"
        
    def dormir(self):
        self.__estado = "Dormido"
    
    def despertar(self):
        self.__estado = "Despierto"
    
    def getEstado(self):
        return self.__estado