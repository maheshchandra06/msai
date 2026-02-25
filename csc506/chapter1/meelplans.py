import sys, operator, random
from pathlib import Path
from nutrition import Food, MealPlan

# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000

def load_nutrient_data(filename: str = "food_data_small.txt"):
    # Open file, read food items one line at a time,
    data_path = Path(__file__).with_name(filename)
    with data_path.open(mode='r', encoding='utf-8') as file:
        food_list = []
        for line_num, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line: continue

            left, seperator, right = line.partition(':')
            if seperator != ":" :
                raise ValueError(f"Invalid line format on line {line_num}: missing ':' -> {raw_line!r}")

            name = left.strip()
            nutrient_parts = [part.strip() for part in right.split(',')]
            if len(nutrient_parts) != 4:
                f"Invalid format on line {line_num}: expected 4 nutrient values "
                f"(protein, carbs, fat, calories) -> got {len(nutrient_parts)}: {nutrient_parts}"

            # create Food objects and append them to a list.
            try:
                protien = float(nutrient_parts[0])
                carbs = float(nutrient_parts[1])
                fat = float(nutrient_parts[2])
                calories = float(nutrient_parts[3])
            except ValueError as e:
                raise ValueError(f"Invalid nutrient value on line {line_num}: {e}") from e

            food = Food(name, protien, carbs, fat, calories)
            food_list.append(food)
        print(f"Loaded {len(food_list)} foods from {data_path.name}")
        # Return the list once the entire file is processed.
        print(food_list)
        return food_list

def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    foods.sort(key=operator.attrgetter(nutrient), reverse=True)
    print(f"Sorted food list by {nutrient} {foods}")
    return foods

def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()
    foods = sort_food_list(foods, nutrient)

    for food in foods:
        sum_calories = plan.calories_with_food(food)
        sum_percent = plan.percent_nutrient_with_food(food, nutrient)
        sum_fraction = plan.fraction_to_fit_nutrient_goal(food, nutrient, goal)
        if sum_calories < MAX_CALORIES and sum_percent < goal and sum_fraction > FRACTION_THRESHOLD:
            plan.add_food(food)
        else:
            food.set_fraction(plan.fraction_to_fit_calories_limit(food, MAX_CALORIES - sum_calories))
            plan.add_food(food)

    return plan

def print_menu():
    print("\nEnter name of food data file: food_data_small.txt\n")
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbohydrates")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()

if __name__ == "__main__":
    # 1. Load the food data from the file
    foods = load_nutrient_data()

    print_menu()
    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    choice_index = int(input("Enter your choice (1-4): "))
    print(choice_index)
    choices = ['protein','carbohydrates','fat']
    input_choice = choices[choice_index-1]

    nutrient = choices[choice_index-1]

    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)
    goal = int(input(f"What percentage of calories from {input_choice} is the goal? : "))

    # 4. Run greedy algorithm to create the meal plan.
    plan = create_meal_plan(foods, nutrient, goal)

    # 5. Display plan.
    print(plan)