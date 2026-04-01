linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
maiorAB = (a + b + abs(a - b)) // 2
resultado = (maiorAB + c + abs(maiorAB - c)) // 2
print(f"{resultado} eh o maior")
