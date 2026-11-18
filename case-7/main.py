# Project 07: String-Based Examination Answer Evaluation
answer_key = ["python", "cpu", "input", "list", "loop"]
score = 0

print("ANSWER EVALUATION")
print("Answer the following 5 questions.")

for question in range(1, 6):
    student_answer = input("Question " + str(question) + ": ")
    normalized_answer = student_answer.strip().lower()

    if normalized_answer == answer_key[question - 1]:
        print("Correct answer.")
        score = score + 2
    else:
        print("Incorrect answer.")

percentage = score / 10 * 100
print("\nFinal score:", score, "/ 10")
print("Percentage:", percentage, "%")
