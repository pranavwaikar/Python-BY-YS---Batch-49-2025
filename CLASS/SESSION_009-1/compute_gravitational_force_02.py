m1 = float(input('Enter the mass of object 1 in kgs: '))
m2 = float(input('Enter the mass of object 2 in kgs: '))
r = float(input('Enter the distance between the objects in meters: '))
G = 6.67 * 10 ** -11
F = (G * m1 * m2)/(r ** 2)
print('Gravitaional force:',F,'Newton')
