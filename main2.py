import random
class FruitQuiz:
    def __init__(self):
        self.fruit_colors={
            "apple":"red",
            "mangoes":"Yellow",
            "banana":"yellow",
            "grapes":"purple",
            "pineapple":"yellow",
            "watermelon":"green",
            "peaches":"orange",
            "cherries":"red",
            "pears":"green",
            "oranges":"orange",
        }
    def start_quiz(self):
        fruits = random.choice(list(self.fruit_colors.keys()))
        correct_color = self.fruit_colors[fruits].lower()

        user_input = input(f"What's the color of a {fruits}? ").strip().lower()
        if user_input == correct_color:
            print("Correct! 😂😂😂😂😂😂")
        else:
            print(f"Incorrect, the correct color is {correct_color}.")

quiz=FruitQuiz()
quiz.start_quiz()     
