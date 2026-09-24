def load_questions():
    questions = []

    try:
        with open("questions.txt", "r") as file:

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                question = parts[0]
                options = parts[1:5]
                correct_answer = int(parts[5])

                questions.append({
                    "question": question,
                    "options": options,
                    "answer": correct_answer
                })

    except FileNotFoundError:
        print("questions.txt was not found.")

    return questions


def display_question(question_number, question_data):
    print("\n------------------------------")
    print(f"Question {question_number}")
    print("------------------------------")

    print(question_data["question"])

    for number, option in enumerate(question_data["options"], start=1):
        print(f"{number}. {option}")


def get_answer():
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))

            if 1 <= answer <= 4:
                return answer

            print("Please choose a number from 1 to 4.")

        except ValueError:
            print("Please enter a valid number.")


def run_quiz(questions):
    score = 0

    for question_number, question_data in enumerate(questions, start=1):

        display_question(question_number, question_data)

        user_answer = get_answer()

        if user_answer == question_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print(
                f"The correct answer was "
                f"option {question_data['answer']}."
            )

    return score


def display_result(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\n==============================")
    print("         QUIZ RESULT")
    print("==============================")

    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {total_questions - score}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 70:
        print("Result: Passed")
    else:
        print("Result: Failed")


def main():
    print("==============================")
    print("      MULTIPLE-CHOICE QUIZ")
    print("==============================")

    questions = load_questions()

    if len(questions) == 0:
        print("No questions available.")
        return

    score = run_quiz(questions)

    display_result(score, len(questions))


main()