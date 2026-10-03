class student:
    grade = 9
    name = "V.Yashwanth"

    def introduce(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I'm in grade ", self.grade)

ob = student()
ob.introduce()
ob.details()