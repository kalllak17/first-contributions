# a
"""
Author: Arkdaii Akopian
Assignment: #1
"""

# b
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# c
# dictionary with str as a key and tuple as a value
workout_stats = {"Alex": (30, 40, 20), "Jamie": (45, 30, 20), "Taylor": (20, 16, 88)}

# d
workout_total = {}
for key, value in workout_stats.items():
    total = sum(value)
    workout_total[f"{key}_Total"] = total

# e
# 2d array of int
workout_list = [list(value) for value in workout_stats.values()]

# f
yoga_running_all = [row[:2] for row in workout_list]
print(f"Minutes for yoga and running for all friends: {yoga_running_all}")
weightlifting_last_two = [row[2] for row in workout_list[1:3]]
print(f"Minutes for weightlifting for the last two friends: {weightlifting_last_two}")

# g.
for key, value in workout_total.items():
    if value > 120:
        ind = key.find("_")
        name = key[:ind]
        print(f"Great job staying active, {name}!")

# h.
inputted_name = input("Enter name ").capitalize()
if inputted_name in workout_stats:
    print(f"{inputted_name} has {workout_stats[inputted_name]}. Total: {sum(workout_stats[inputted_name])}")
else:
    print(f"Friend {inputted_name} not found in the records.")

# i.
highest_friend, highest_total = max(workout_total.items(), key=lambda x: x[1])
print(    f"The friend with the highest total workout minutes {highest_total} "
          f"is {highest_friend[:highest_friend.find("_")]}.")
lowest_friend, lowest_total = min(workout_total.items(), key=lambda x: x[1])
print(f"The friend with the lowest total workout minutes {lowest_total} is {lowest_friend[:lowest_friend.find("_")]}.")
