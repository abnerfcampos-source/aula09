
#nome = input('Digite seu nome: ')
#idade = int(input('Digite seu idade: '))
#altura = float(input("Digite sua altura: "))
#peso = float(input("Digite seu peso: "))
#imc = peso / altura ** 2
#print(f"Meu nome e {nome}, tenho {idade} anos e {altura} de altura.Meu peso é {peso}. IMC{imc: .2f}")

#nome = input("Digite seu nome: ")
#idade = int (input("Digite sua idade: "))
#dps = idade + 10

#print(f"Sua idade é {idade}, sua idade daqui 10 anos é {dps}")

# temp = int (input("Digite a temperatura: "))
# fr = temp * 9/5 + 32

# print(f"A conversao de celsios para fahrenheit é: {fr} fahrenheit")

# base = int (input("Base do retangulo: "))
# haltura = int (input("Largura do retangulo: "))

# area = (haltura + base) * 2

# print(f"A area é: {area}")

# nota1 = int (input("escreva primera nota:"))
# nota2 = int (input("escreva segunda nota:"))
# nota3 = int (input("escreva terceira nota:"))
# media = (nota1 + nota2 + nota3) / 3

# print(f"Sua media é; {media}")
nome = input('Digite seu nome: ')
idade = int(input('Digite seu idade: '))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / altura ** 2
print(f"Meu nome e {nome}, tenho {idade} anos e {altura} de altura.Meu peso é {peso}. IMC{imc: .2f}")

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura**2

if imc < 18.5:
        print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
        print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso.')
elif imc >= 30 and imc <= 34.9:
        print('Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
        print('Obesidade grau II')
else:
        print('Obesidade grau III')