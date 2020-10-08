from actor import Actor
from role import Role
from show import Show


actors = [
    Actor("Иванов Иван Иванович", "Иванов И.И.", 5, 3),
    Actor("Петров Пётр Петрович", "Петров П.П.", 5, 1),
    Actor("Сидоров Сидор Сидорович", "Сидоров С.С.", 6, 2),
    Actor("Ололоева Ололёна Ололоевна", "Ололоева О.О.", 6, 2),
    Actor("Пионер Семён Анонович", "Пионер С.А.", 7, 0)
]

roles = [
    Role("Клавдий", actors[0]),
    Role("Гамлет", actors[1]),
    Role("Полоний", actors[2]),
    Role("Горацио", actors[3]),
    Role("Лаэрт", actors[4])
]

show = Show("Гамлет", 1600, 100000, roles)

print("Актёры:")
for actor in actors:
    print(actor)

print("\nРоли:")
for role in roles:
    print(role)

print("\nСпектакль:")
print(show)

sum = 0
print("\nСмета:")
for role in roles:
    sum += role.getContractValue()
    print("{}: {}".format(role.getName(), role.getContractValue()))

print("\nИтого: " + str(sum))
