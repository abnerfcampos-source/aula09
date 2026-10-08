import random

# numero_secreto = 67
# chute = int (input("escolha um numero de 1 a 10: "))
# print(f"Voce escolheu o numero: {chute}")

# if chute == numero_secreto:
#         print("Voce acertou Parabens!!!")
# elif chute > numero_secreto:
#         print("Voce errou, Tente um numero menor")
# else:
#         print("Voce errou, Tente um numero maior")

numero_secreto = random.randint(1, 20)
tentativas = 0 

print('Tente adivinhar o numero que estou pemsando... Entre 1 e 20. Voce tem 5 tentativas')

# while True:
#         chute = int(input('Seu palpite: '))
#         tentativas +=1
#         if chute < numero_secreto:
#                 print('Voce errou! Tente um numero maior')
#         elif chute > numero_secreto:
#                 print("Voce errou! Tente um numero menor")
#         else:
#                 print(f"Voce acertou em {tentativas} tentiva(s)!!! Parabens")
#                 break

for tentativa in range (1,6):
        chute = int (input("Seu palpite: "))

        if chute < numero_secreto:
                print('Voce errou! Tente um numero maior')
        elif chute > numero_secreto:
                print("Voce errou! Tente um numero menor")
        else:
                print(f"Voce acertou em {tentativa} tentiva(s)!!! Parabens")
                break
else:
        print(f"Acabaram as tentativas. O numero era {numero_secreto}")
    