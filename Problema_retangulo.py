import math
base = float(input("Qual a base do retangulo: "))
altura = float(input("Qual a altura do retangulo: "))

area = base * altura
perimetro = 2*(base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"A área do retangulo é: {area:.4f}")
print
print(f"O perimetro do retangulo é: {perimetro:.4f}")
print
print(f"A diagonal do retangulo é: {diagonal:.4f}")
