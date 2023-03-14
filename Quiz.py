# Quiz game script

# Create a list of questions and their answers
questions = {
    "What is the capital of France? ": "Paris",
    "What is the largest country in the world by land area? ": "Russia",
    "What is the highest mountain in the world? ": "Mount Everest",
    "What is the currency of Japan? ": "Yen",
    "What is the largest organ in the human body? ": "Skin"
}

# Initialize a variable to keep track of the number of correct answers
score = 0

# Loop through the questions and ask them one by one
for question, answer in questions.items():
    # Get the user's answer
    user_answer = input(question)

    # Check if the user's answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is: ", answer)

# Print the final score
print("Your final score is: ", score, " out of ", len(questions))
