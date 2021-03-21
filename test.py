class stu_info:
    def __init__(self, number, name):
        self.number = number
        self.name = name

class Test(stu_info):
    def __init__(self, number, name, subject, score):
        super(Test, self).__init__(number, name)
        self.subject = subject
        self.score = score

    @property #when you use property, google it!
    def read_number(self):
        return self._number

    def printer(self):
        print(self.number, self.name, self.subject, self.score)

    def evaluate(self):
        if self.score > 90:
            evaluation = "A"
        elif (self.score <= 90) and (self.score > 60):
            evaluation = "B"
        else:
            evaluation ="C"
        return evaluation

class list_test:
    def __init__(self):
        self.test_list = []

    def input_data(self):
        for i in range(10):
            self.test_list.append(i)

    def show_data(self):
        for i in range(len(self.test_list)):
            print(self.test_list[i])


def main():
    kouki = Test(1, "kouki", "kokugo", 89)
    kouki.printer()
    kouki = Test(2, "uchibori", "suugaku", 90)
    kouki.printer()
    a = list_test()
    b = []
    b.append(1)
    print(b)

    a.input_data()
    a.show_data()
    a.test_list.append(1)
    a.show_data()





if __name__ == "__main__":
    main()



