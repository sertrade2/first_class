from masina import Car

masina1 = Car('Audi', 53.20, 9.6)

print(masina1)
print(masina1.drive(50))

masina1.refuel(20)
print(masina1)
print(masina1.can_drive(2000))
print(masina1.get_fuel())