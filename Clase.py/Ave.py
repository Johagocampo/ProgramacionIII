from Actividad1 import Animal
class Ave(Animal): 
    def __init__(self, nombrex, pesox, año_nacimiento, propietario):
        self.año_nacimientox= año_nacimiento
        self.propietariox= propietario
        super().__init__(nombrex, pesox)
    def printAÑO(self):
        print(self.año_nacimiento, self.propietario)

    def edad(self):
        edad= 2024 - self.año_nacimientox
        print("El nombre del animal es:", self.nombrex)
        print("Su edad es: ",edad )
        
       
        if (edad>=5):
            print("El animal es mayor de edad")
        else:
            print("El animal es menor de edad")
        
        print("El nombre del propietario es:" , self.propietariox)
               
Ave1= Ave("Pepe", 20, 2020, "Johana")
Ave1.edad()

