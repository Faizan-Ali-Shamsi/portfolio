print("How many steps did you walk?")

steps_str = input("Steps: ")
weight_str = input("Your body weight (kg): ")
gender = input("Enter your gender: ")

if steps_str.isdigit() and weight_str.isdigit():
    steps = int(steps_str)
    weight = int(weight_str)

    if gender.lower() == "male":

        distance = (steps * 0.85) / 1000
        calories_burned = distance * weight * 0.9

        print(
            f"You've burned {calories_burned: .2f} calories. Keep it up champ!")

    elif gender.lower() == "female":

        distance = (steps * 0.78) / 1000
        calories_burned = distance * weight * 0.9

        print(
            f"You've burned {calories_burned: .2f} calories. Keep it up champ!")

    else:
        print("I said enter your gender not illness.")

else:
    print("Input numerics only!")
