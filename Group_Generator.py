import random

names = ["Adrian", "Alejandro", "Elias", "Ivan", "Jhover", "Joan", "Jiale", "Oriol", "Ramiro", 
         "Pau", "Leandro", "Darío", "Marc", "Victor", "Yeray", "Nasir", "Izan R", 
         "Alexey", "Alex", "Izan V"]

groups = []

while len(names) > 1:
    random.shuffle(names)
    name_1 = names.pop(0)   # Take the first name
    name_2 = names.pop(-1)  # Take the last name
    groups.append([name_1, name_2])  # Create and store the group

# If there's one person left, put them in a solo group
if names:
    groups.append([names.pop()])

# Display the results
for i, group in enumerate(groups, 1):
    print(f"Group {i}: {', '.join(group)}")




        



