from models.certificate import Certificate
grade = input("what is your grade? e.g. 10 : ")
major = input("what is your major? e.g. Mathematics : ")
typ = int(input("Do you want to calculate your score by:\n1) Your Missing \n2) Your Total Score\n >>>"))

if typ == 1:
    Certificate.calc_by_missing(grade,major)
else:
    Certificate.calc_by_score(grade, major)