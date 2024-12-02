from model import generate

prompt = """
Generate one {Category} Aptitude MCQ question related to the topic {topic} and provide only the correct option letter.
"""


def helper(Category_name, topic_name, no_of_questions):
    total_questions = no_of_questions
    correct_answers = 0
    user_answers = []
    actual_answers = []
    prompt = prompt.format(Category=Category_name, topic=topic_name)
    for i in range(total_questions):
        question_text = generate(prompt)

        try:
            correct_option = (
                question_text.split("Correct option: ")[1][0].strip().lower()
            )
        except IndexError:
            print(f"Error fetching correct answer for question {i + 1}")
            continue
        actual_answers.append(correct_option)
        question_display = question_text.split("Correct option: ")[0]
        print(f"Question {i + 1}: {question_display}")
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()
        user_answers.append(user_answer)
    correct_answers = sum(
        [1 for i in range(total_questions) if user_answers[i] == actual_answers[i]]
    )
    print(
        f"\nYou answered {correct_answers} out of {total_questions} questions correctly.\n"
    )
    print("Correct answers were:")
    for i in range(total_questions):
        print(f"Question {i + 1}: Correct answer is {actual_answers[i].upper()} and Your answer is {user_answers[i].upper()}")
