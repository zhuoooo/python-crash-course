pizzas = ['A', 'B', 'C', 'D', 'E', 'F']

for p in pizzas[:3]:
    print('I like ' + p + ' pizza')

print('I really love pizza!')

more_pizzas = pizzas[:]
more_pizzas.append('chicken')
print(more_pizzas)