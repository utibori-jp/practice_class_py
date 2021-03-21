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


class Clinic:
    def __init__ (self):
        self.reservation_list = []

    def show_waiting_count(self):
        print("now waiting {} people".format(len(self.reservation_list)))

    def check_reserved(self, name):
        for i in range(len(self.reservation_list)):
            if self.reservation_list[i] == name:
                return True
            else:
                return False

    def reserve(self, name):
        if self.check_reserved(name):
            print("you'veb already reserved")
        else:
            self.reservation_list.append(name)
            print("your reservation is done")

    def diagnosis(self, name = None):
        if (name):
            print("ok!")
        else:
            #koredato <__main__.Patient object at 0x0000024C5DBD0A90> mitainanogaderu
            # print(self.reservation_list)
            self.reservation_list.pop(0)

    @staticmethod
    def run ():
        pass



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

    Clinic.run()


if __name__ == "__main__":
    main()

