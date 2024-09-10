print("introduccion a clases")
class animal:
    edad=3 
    raza="chihuahua"
    comida="croquetas"
    def come(self):
        print(f"el perro come {self.comida}")
print(animal)
print("creando el objeto de la clase animal")
perro=animal()
print(f"la edad del perro es {perro.edad}")
print(f"la raza del perro es {perro.raza}")
perro.come()


