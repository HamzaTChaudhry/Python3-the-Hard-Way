# ex5: More Variables and Printing

name = 'Hamza T. Chaudhry'
age = 22 # not a lie
height = 74 # inches
metric_height = height * 2.54 # centimeters
weight = 175 # lbs
metric_weight = weight / 2.2 # kgs
eyes = 'Dark Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {metric_height} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {metric_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")