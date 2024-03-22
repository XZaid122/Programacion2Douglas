lista = []
animales = ['gato', 'perro', 'conejo', 'tortuga', 'loro', 'pez']
print ('lista:', lista)
print ('lista:', len(lista))
print ('animales:', (animales))
print ('animales:', len(animales))

animales = ['gato', 'perro', 'conejo', 'tortuga', 'loro', 'pez']
print (animales.index('gato'))
print (animales.index('conejo'))
print (animales.index('pez'))

Datos_personales = ['nombre', 'edad', 'altura', 'estado civil', 'direccion']
Datos_personales.append('cedula')
print ('Datos personales', Datos_personales)
print ('Datos personales:', len(Datos_personales))

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(7, 'Whatsapp')
print ('Empresas:', it_companies)
Existe = 'Facebook' in it_companies
print (Existe)
it_companies.sort ()
print (it_companies)
it_companies.sort (reverse=True)
print (it_companies)
it_companies.pop (0)
print (it_companies)
del it_companies [0]
print (it_companies)
it_companies.clear ()
print (it_companies)