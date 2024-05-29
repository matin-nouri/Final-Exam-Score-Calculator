from models.data_parser import JsonParser


class Certificate:
    def __init__(self):
        pass

    @staticmethod
    def calc_by_score(grade, major):
        js = JsonParser(f"{grade}th Grade Coefficient").read()
        result = 0
        index = js[major]
        for i in index:
            for j in i:
                sc = float(input(f"What is your score for {j}? "))
                result += sc * (i[j]) / 37
        print(result)

    @staticmethod
    def calc_by_missing(grade, major):
        js = JsonParser(f"{grade}th Grade Coefficient").read()
        result = 20
        index = js[major]
        for i in index:
            for j in i:
                sc = float(input(f"lost score for {j} : "))
                result -= sc * (i[j]) / 37
        print(result)