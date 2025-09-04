#clase persona
class Persona:
    nombre=""
    Edad=0
    altura=0
    genero=""

    def caminar(self):
        return f"Hola soy {self.nombre} y Me encuentro caminando..."


#persona1 -> objeto  Persona()->CLASE
persona1=Persona()
persona2=Persona()
persona3=Persona()
persona1.nombre="Alexander"
persona2.nombre="Mercedes Maria Alexandra"
persona3.nombre="Diana Esther"

print(persona1.nombre)
print(persona1.caminar())

