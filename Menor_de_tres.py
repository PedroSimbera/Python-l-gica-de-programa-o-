num1 = int(input("Informe a primeira idade: "))
num2 = int(input("Informe a segunda idade: "))
num3 = int(input("Informe a terceira idade: "))

if num1 < num2 and num1 < num3:
    menor = num1
    print("Menor idade: ", menor)

elif num2 < num3:
    menor = num2
    print("Menor idade: ", menor)

else:
    menor = num3
    print("Menor idade: ", menor)