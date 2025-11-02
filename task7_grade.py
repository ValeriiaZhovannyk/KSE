def get_letter_grade(score):
    """
    Convert score to letter grade.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    """
    letter_scores = ['A', 'B', 'C', 'D', 'F']
    score_convertion = (99-int(score))//10
    converted_score = letter_scores[score_convertion]
    return(converted_score)


print(get_letter_grade(95))  # "A"
print(get_letter_grade(82))  # "B"
print(get_letter_grade(55))  # "F"