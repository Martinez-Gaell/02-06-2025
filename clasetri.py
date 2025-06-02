class Triangulo:
    def __init__(self):
        # Ya definido: atributos base y altura
        self.base = 0
        self.altura = 0

  # Crea una función dentro de la clase llamada `leer_datos` que reciba como argumento a sí misma usando la palabra clave `self`.
    # Dentro de esta función, solicita al usuario que ingrese la base del triángulo y guarda ese valor en un atributo llamado `self.base`.
    # Luego, solicita al usuario que ingrese la altura del triángulo y guarda ese valor en el atributo `self.altura`.
    # Asegúrate de convertir ambos valores a tipo `float` usando la función `float()`.

    def leer_datos(self):
        self.base = float(input("ingrese el valor de la base\n"))
        self.altura = float(input("ingrese el valor de la altura\n"))

 # Crea una función llamada `calcular_area` que retorne el resultado de (base * altura) / 2 usando los atributos del objeto.

    def calcular_area(self):
        r = (self.base * self.altura)/2
        print("el area es: ",r)

# Crea un objeto llamado `t` a partir de la clase `Triangulo`.
# Llama al método `leer_datos` con ese objeto.
# Imprime el resultado de `calcular_area()`.

t = Triangulo()
t.leer_datos()
t.calcular_area()
