import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""
# start-->
def multiplicar(num1, num2):
    result = num1 * num2
    return result

multiplicar(2, 4)


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""

# start-->
def sumaDivTresYCinco():
    i = 0
    suma = 0
    while i <= 1000:
        if i % 3 == 0 and i % 5 == 0:
            suma = suma + i
        elif i % 3 == 0:
            suma = suma + i
        elif i % 5 == 0:
            suma = suma + i
        else:
            pass

        i += 1

    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
radio = 5
altura = 11

definicionCono(radio, altura)

def definicionCono(radio, altura):
    generatriz = obtenerGeneratriz(radio, altura)
    area = obtenerArea(radio, altura)
    volumen = obtenerVolumen(radio, altura)
    result = {"generatriz" : generatriz, "area" : area, "volumen" : volumen }
    return result


def obtenerGeneratriz(radio, altura):
    # square_root(altura^2 + radio^2)
    result = math.sqrt((altura ** 2) + (radio ** 2))
    return result


def obtenerArea(radio, altura):
    # pi*radio*(radio+generatriz)
    result = (math.pi) * radio * (radio + (math.sqrt((altura ** 2) + (radio ** 2))))
    return result


def obtenerVolumen(radio, altura):
    # (1/3)*pi*radio^2*altura
    result = (1 / 3) * (math.pi) * (radio ** 2) * altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def definicionCono(self):
        self.radio = 5
        self.altura = 11
        generatriz = self.obtenerGeneratriz(self.radio, self.altura)
        area = self.obtenerArea(self.radio, self.altura)
        volumen = self.obtenerVolumen(self.radio, self.altura)
        result = {"generatriz" : generatriz, "area" : area, "volumen" : volumen }
        return result

    def obtenerGeneratriz(self, radio, altura):
        # square_root(altura^2 + radio^2)
        result = math.sqrt((altura ** 2) + (radio ** 2))
        return result

    def obtenerArea(self, radio, altura):
        # pi*radio*(radio+generatriz)
        result = (math.pi) * radio * (radio + (math.sqrt((altura ** 2) + (radio ** 2))))
        return result

    def obtenerVolumen(self, radio, altura):
        # (1/3)*pi*radio^2*altura
        result = (1 / 3) * (math.pi) * (radio ** 2) * altura
        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:
    def registrar(self):
        return 0

    def totalCostoSanSalvador(self):
        return 0

    def totalCostoConDescuento(self):
        return 0


class Paciente:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
