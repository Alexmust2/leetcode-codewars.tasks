def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) // 3
    if score <= 100 and score >= 90 :
        return "A"
    if score < 90 and score >= 80:
        return "B"
    if score < 80 and score >= 70:
        return "C"
    if score < 70 and score >= 60:
        return "D"
    return "F"


print(get_grade(70, 70, 100))