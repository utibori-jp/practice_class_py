class Human:
    def __init__(self, name):
        self.name = name

class Patient(Human):
    def __init__(self, name, symptom, patient_id):
        super(Patient, self).__init__(name)
        self.symptom = symptom
        self.patient_id = patient_id

    def show_data(self):
        print(self.name, self.symptom, self.patient_id)

    #objectを指定して、そのままpinrtするときの書式を指定できる。line44のような書き方をせずとも、情報をprint出来る
    def __str__ (self):
        return f"{self.name} {self.symptom}{self.patient_id}"


class Clinic:
    def __init__ (self):
        self.reservation_list = []

    def show_waiting_count(self):
        print("now waiting {} people".format(len(self.reservation_list)))

    def check_reserved(self, name:Patient):
        for i in range(len(self.reservation_list)):
            if self.reservation_list[i] == name:
                return True
            else:
                return False

    def reserve(self, name:Patient):
        if self.check_reserved(name):
            print("you've already reserved")
        else:
            self.reservation_list.append(name)
            print("your reservation is done")

    def diagnosis(self, name:Patient = None):
        if (name):
            print("ok!")
        else:
            self.reservation_list[0].show_data()
            self.reservation_list.pop(0)


def main():
    myclinic = Clinic()

    #patient data
    sato = Patient("sato", "cough", 111)
    tanaka = Patient("tanaka", "stomachache", 222)
    suzuki = Patient("suzuki", "runny-nose", 333)
    yamada = Patient("yamada", "makaise", 444)
    kouki = Patient("kouki", "back-pain", 555)

    #reserve
    myclinic.reserve(sato)
    myclinic.reserve(kouki)
    myclinic.reserve(suzuki)
    myclinic.reserve(sato)
    #show the number of people waiting for a medical examination
    myclinic.show_waiting_count()

    #diagnosis
    myclinic.diagnosis()
    #check the number of people waiting for a medical examination
    myclinic.show_waiting_count()
    # print(type(myclinic.reservation_list))

    #__str__を用いたprint方法
    print (sato)


if __name__ == "__main__":
    main()

