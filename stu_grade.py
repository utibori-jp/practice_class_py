class Score:
    def __init__(self, name, math, english, japanese):
        self.name = name
        self.math = math
        self.english = english
        self.japanese = japanese

    def __str__(self):
        return f"{self.name} {self.math} {self.english} {self.japanese}"


class Grade_mng:
    def __init__(self):
        self.stu_data = []

    def set_data(self, student:Score):
        self.stu_data.append(student)

    def show_data(self):
        for i in range(len(self.stu_data)):
            print(self.stu_data[i])

    def best_stu_math(self):
        best_score_math = 0
        for i in range(len(self.stu_data)):
            math_score = self.stu_data[i].math
            if best_score_math < math_score:
                best_score_math = math_score
        return best_score_math

    def best_subject_each_student(self):
        best_score = 0
        for i in range(len(self.stu_data)):
            best_sub = "math"
            best_score = self.stu_data[i].math

            if best_score < self.stu_data[i].japanese:
                best_sub = "japanese"
                best_score = self.stu_data[i].japanese
            if best_score < self.stu_data[i].english:
                best_sub = "english"
                best_score = self.stu_data[i].english

            print(f"{self.stu_data[i].name} {best_sub} {best_score}")


def main():
    taro = Score("taro", 60, 70, 80)
    jiro = Score("jiro", 80, 70, 90)
    saburo = Score("saburo", 50, 30, 60)

    grade_list = Grade_mng()

    grade_list.set_data(taro)
    grade_list.set_data(jiro)
    grade_list.set_data(saburo)

    grade_list.show_data()
    # print(grade_list.best_stu_math())
    # print(jiro)
    grade_list.best_subject_each_student()

if __name__ == "__main__":
    main()


