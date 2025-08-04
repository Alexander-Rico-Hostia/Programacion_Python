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
persona1.nombre="Alexander"

print(persona1.nombre)
print(persona1.caminar())

