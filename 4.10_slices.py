cubes = [val ** 3 for val in range(1, 11)]
print(cubes)

first_three = cubes[0:3:1]
print(f"\nThe first three items in the list are {first_three}.")

middle_three = cubes[4:7:1]
print( f"\nThe middle three items in the list are {middle_three} ")

last_three = cubes[-3::1]
print(f"\nThe last three items in the list are {last_three}")