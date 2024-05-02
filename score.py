scores = [40, 45, 50, 60, 70, 100, 0]

student_name = str(input("Enter your name:"))
try:
    if student_name.isalpha():
        user_name = student_name.upper()
        print(user_name)
    else:
        raise ValueError("Enter a valid name")
except ValueError:
    print("Enter a valid name")


def student(score):
    if score >= scores[4] and score <= scores[5]:
        return "A"
    elif score >= scores[3] and score <= scores[4]:
        return "B"
    elif score >= scores[2] and score <= scores[3]:
        return "C"
    elif score >= scores[1] and score <= scores[2]:
        return "D"
    elif score > scores[0] and score <= scores[1]:
        return "E"
    elif score >= score[6] and score <= score[0]:
        return "F"
    else:
        return "Input a valid"

score = int(input("Enter a valid score:"))

def user_score():
    all_scores = list(range(101))
    if score in all_scores:
        return score

try:
    print(user_score(), student(score))
except ValueError:
    print("Enter a valid score:")

                   
