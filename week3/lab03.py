# Import the random library to use for the dice later
import random


# week 3 task 3 start {
def userInputValidation(min, max, msg):
    while True:
        try:
            combatStrength = int(input(f"{msg} (Number between {min}-{max}) "))
            if (combatStrength < min or combatStrength > max):
                print(f"Input must be an integer between {min}-{max}")
            return combatStrength
        except ValueError:
            print("Invalid input")


# } week 3 task 3 end

# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# week03 task 1 start{
diceOptions = list(range(7))  # week03 task 1
# }week03 task 1 end


weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
# week 3 task 2 start {
print("Available weapons: ")
for i in range(0, len(weapons)):
    print(str(i + 1) + ". " + str(weapons[i]))
# } week 3 task 2 end

# week 3 task 3 start {
combatStrength = userInputValidation(1, 6, "Enter your combat Strength: ")
mCombatStrength = userInputValidation(1, 6, "Enter the monster's combat Strength: ")
# } week 3 task 3 end
# week 3 task 4 start {
for j in range(1, 21, 2):
    if j == 11:
        print(f"Battle Truce declared in Round 11. Game Over!")
    else:
        print(f"Round {j}:")
        input("Roll the dice for your health points (Press enter)")
        healthPoints = random.choice(diceOptions)
        print("You rolled " + str(healthPoints) + " health points")

        input("Roll the dice for the monster's health points (Press enter)")
        mHealthPoints = random.choice(diceOptions)
        print("You rolled " + str(mHealthPoints) + " health points for the monster")

        input("Roll the dice to see if you find a healing potion (Press enter)")
        healingPotion = random.choice([0, 1])
        print("Have you found a healing potion?: " + str(bool(healingPotion)))

        # Roll the dice (1-6) to choose which weapon you must use. Save the roll in a variable called weaponRoll.
        weaponRoll = random.choice([0, 1])

        # Add your weaponRoll to the hero's combat strength
        combatStrength += weaponRoll

        # Use this variable as an index into the weapons array and print out the name of the hero's weapon.
        print("The name of the hero's weapon is: " + weapons[weaponRoll])

        # if weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend")
        # But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
        elif weaponRoll <= 4:
            print("Your weapon is meh")
        # Else, print out "Nice weapon, friend! "
        else:
            print("Nice weapon, friend! ")

        # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
        if weapons[weaponRoll] != "Fist":
            print("Thank goodness you didn't roll the Fist...")

        input("Analyze the roll (Press enter)")
        # Equality operators
        print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

        # Relational operators
        print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

        # and keyword
        print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

        # not keyword
        print("--- Phew, you have a healing potion: " + str(
            not (  # monster will NOT kill hero in one blow
                    healthPoints < mCombatStrength  # monster will kill hero in one blow
            )
            and
            healingPotion == 1  # hero has a healing potion
        ))

        # or keyword
        print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

        # in keyword
        print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

        # --- Expanded if statement
        if healthPoints >= 5:
            print("--- Your health is ok")
        elif healingPotion == 1:
            healingPotion = 0
            healthPoints = 6
            print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
        else:
            print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

        # --- Nested if statement
        print("You meet the monster. FIGHT!!")
        input("You strike first (Press enter)")

        print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
        if combatStrength >= mHealthPoints:
            mHealthPoints = 0
            print("You've killed the monster")
        else:
            mHealthPoints -= combatStrength

            print("You've reduced the monster's health to: " + str(mHealthPoints))

            print("The monster strikes!!!")
            print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
            if mCombatStrength >= healthPoints:
                healthPoints = 0
                print("You're dead")
            else:
                healthPoints -= mCombatStrength
                print("The monster has reduced your health to: " + str(healthPoints))

# } week 3 task 4 end
