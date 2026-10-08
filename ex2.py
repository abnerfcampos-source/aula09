filme = ["homem-aranha","vingadores-ultimato","avatar","batman","vingadores-Doom-day"]
print(filme[0], filme[-1],len(filme))

numeros = []
for i in range(5):
    numeros.append(int(input(f"Numero {i + 1}:")))
print(f'Maior: {max(numeros)}| Menor: {min(numeros)}| Soma: {sum(numeros)}')