fav_pizzas = ['cheese', 'tomato', 'pepperoni']

friend_pizzas = fav_pizzas[:]

fav_pizzas.append('mushroom')
friend_pizzas.append('pineapple')

print(fav_pizzas)
print(friend_pizzas)

print(f"My fav pizzas are:.")
for fav_pizza in fav_pizzas:
    print(fav_pizza)
   
print(f"My fav pizzas are:.")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
   