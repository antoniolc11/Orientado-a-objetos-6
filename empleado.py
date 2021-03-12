class Empleado:
    def __init__(self, nombre, apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def nombre_completo(self):
        return f'{self.nombre()} {self.apellidos()}'

    def email(self):
        return f'{self.nombre()}.{self.apellidos()}@company.com'.lower()



emp1 = Empleado('Juan', 'Pérez')
emp2 = Empleado('María', 'García')
emp3 = Empleado('Antonio', 'González')

print(emp1.nombre_completo())
print(emp2.email())
print(emp3.nombre())
