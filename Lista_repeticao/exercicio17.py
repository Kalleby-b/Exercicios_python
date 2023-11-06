n = int(input('Até qual termo da sequencia deve aparecer? '))
fibonacci = [0,1]
for i in range(1,n):
    fibonacci.append(fibonacci[i] + (fibonacci[i-1]))

escrita = ''
fibonacci.pop(0)
for i in range(len(fibonacci)):
    escrita += str(fibonacci[i])+','

print(escrita+'...')