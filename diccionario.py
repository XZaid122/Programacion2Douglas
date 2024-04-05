perro = {}

perro['nombre'] = 'Doky'
perro['color'] = 'Necgro'
perro['Raza'] = 'Pinscher'
perro['patas'] = 4
perro['edad'] = 2
print(perro)

estudiante = {
    
    'nombre' : 'Douglas',
    'apellido' : 'Araujo',
    'sexo' : 'Masculino',
    'estado civil' : 'Soltero',
    'habilidades' : ['Java', 'Python',],
    'pais' : 'Colombia',
    'ciudad' : 'Cartagena',
    'direccion' : 'Crespito cra 14 69a06'      
}
print(estudiante)
print(len(estudiante))
print(estudiante['habilidades'])
estudiante['habilidades'].append('PHP')
print(estudiante['habilidades'])
keys = estudiante.keys()
print(keys)
values = estudiante.values()
print(values)
print(estudiante.items())
estudiante.pop('direccion')
print(estudiante)
print(estudiante.clear())