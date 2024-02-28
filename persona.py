class persona:
    def __init__(self, nombre, apellido, cedulaint, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedulaint = cedulaint
        self.correo = correo 
        self.telefono = telefono
    def obtenernombre (self):
        return f'mi nombre es {self.nombre} {self.apellido}'
    def obtenercedulaint (self):
        return f'mi cedula es {self.cedulaint}'
    def obtenercorreo (self):
        return f'mi correo es {self.correo}'
    def obtenertelefono (self):
        return f'mi telefono es {self.telefono}'

p=persona("Douglas Josue", "Araujo Mendez", "1270319", "douglasjosue31@hotmail.com", "3043099390") 

print(p.obtenernombre(), p.obtenercedulaint(), p.obtenercorreo(), p.obtenertelefono())
