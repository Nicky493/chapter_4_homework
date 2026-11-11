menu = ("crab legs", "ice cream", "salad", "steak", "fried chicken")

print(f"The buffet menu is:")
for food in menu:
    print(food )

try:
    menu[0] = "new value"
except TypeError:
    print(f"\nSorry, the menu can't be changed.\n")

new_menu = ("crab legs", "ice cream", "salad", "grilled chicken", "salmon")

print(f"The revised menu are:")
for food in new_menu:
    print(food)