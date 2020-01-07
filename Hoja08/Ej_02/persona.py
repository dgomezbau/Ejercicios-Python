import itertools

class Persona:

    id_generator = itertools.count(0)

    def __init__(self):
        self.id = next(self.id_generator)
        self.generacion = 0
        self.nombre = None
        self.apellidos = None
        self.fechaNacimiento = None
        self.fechaDefuncion = None
        self.lugarNacimiento = None
        self.lugarDefuncion = None
        self.localResidiencia = []
        self.profesion = None
        self.datosVarios = []
        self.parentescoSangre = True

    def getId(self):
        return self.id

    def getGeneracion(self):
        return self.generacion

    def setGeneracion(self, generacion:int):
        self.generacion = generacion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre:str):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos

    def setApellidos(self, apellidos:str):
        self.apellidos = apellidos

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def setFechaDefuncion(self, fechaDefuncion:str):
        self.fechaDefuncion = fechaDefuncion

    def getLugarNacimiento(self):
        return self.lugarNacimiento

    def setLugarNacimiento(self, lugarNacimiento:str):
        self.lugarNacimiento = lugarNacimiento

    def getLugarDefuncion(self):
        return self.lugarDefuncion

    def setLugarDefuncion(self, lugarDefuncion):
        self.lugarDefuncion = lugarDefuncion
    
    def getLocalResidencia(self):
        return self.localResidiencia

    def setLocalResidencia(self, localizacion:str):
        self.localResidiencia.append(localizacion)

    def getProfesion(self):
        return self.profesion

    def setProfesion(self, profesion:str):
        self.profesion = profesion
    
    def getDatosVarios(self):
        return self.datosVarios

    def setDatosVarios(self, dato:str):
        self.datosVarios.append(dato)

    def getParentescoSangre(self):
        return self.parentescoSangre

    def setParentescoSangre(self, parentescoSangre:bool):
        self.parentescoSangre = parentescoSangre



