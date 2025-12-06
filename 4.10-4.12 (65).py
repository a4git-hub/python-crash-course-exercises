#4.10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following
# apps = ['chrome', 'brave', 'files', 'terminal', 'discord']
# print(f"The first 3 apps are,")
# for app in apps[:3]:
#     print(app.title())

# print(f"The 3 middle apps are,")
# for app in apps[1:4]:
#     print(app.title())

# print(f"The 3 last apps are,")
# for app in apps[2:]:
#     print(app.title())

pizza = ['pepperoni', 'cheese', 'vegetarian']

fried_pizza = ['pepperoni', 'cheese', 'vegetarian']

pizza.append('mushroom')
fried_pizza.append('chicken')

pizza = fried_pizza
for pizzas in pizza:
    print("These are my favorite types of pizza:")

    print(pizzas.title())




