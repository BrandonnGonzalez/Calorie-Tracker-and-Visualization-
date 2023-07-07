from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3100  # kcal
PROTEIN_GOAL = 190  # grams
FAT_GOAL = 85  # grams
CARBS_GOAL = 400  # grams

today = []


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


# Move the while loop inside a function for better structure
def main():
    done = False

    while not done:
        print("""
        (1) Add a new food
        (2) Visualize progress
        (q) Quit
        """)

        choice = input("Choose an option: ")

        if choice == "1":
            print("Adding a new food!")
            name = input("Name: ")
            calories = int(input("Calories: "))
            proteins = int(input("Proteins: "))
            fats = int(input("Fats: "))
            carbs = int(input("Carbs: "))
            food = Food(name, calories, proteins, fats, carbs)
            today.append(food)
            print("Successfully added!")
        elif choice == "2":
            calorie_sum = sum(food.calories for food in today)
            protein_sum = sum(food.protein for food in today)
            fats_sum = sum(food.fat for food in today)
            carbs_sum = sum(food.carbs for food in today)

            # Create a single figure instead of subplots
            fig, axs = plt.subplots(2, 2)

            # Pie chart - Macronutrients Distribution
            axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f")
            axs[0, 0].set_title("Macronutrients Distribution")

            # Bar chart - Macronutrients Progress
            x = np.arange(3)
            width = 0.35
            axs[0, 1].bar(x, [protein_sum, fats_sum, carbs_sum], width, label='Progress')
            axs[0, 1].bar(x + width, [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width, label='Goal')
            axs[0, 1].set_xticks(x + width / 2)
            axs[0, 1].set_xticklabels(["Proteins", "Fats", "Carbs"])
            axs[0, 1].set_title("Macronutrients Progress")
            axs[0, 1].legend()

            # Pie chart - Calories Goal Progress
            axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
            axs[1, 0].set_title("Calories Goal Progress")

            # Line plot - Calories Goal Over Time
            axs[1, 1].plot(range(len(today)), np.cumsum([food.calories for food in today]), label="Calories Eaten")
            axs[1, 1].plot(range(len(today)), [CALORIE_GOAL_LIMIT * len(today)], label="Calorie Goal")
            axs[1, 1].legend()
            axs[1, 1].set_title("Calories Goal Over Time")

            fig.tight_layout()
            plt.show()
        elif choice == "q":
            done = True
        else:
            print("Invalid option. Try again.")


# Call the main function to start the program
if __name__ == "__main__":
    main()
