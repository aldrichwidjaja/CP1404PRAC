class ProgrammingLanguage:
    def __init__(self, coding, type, reflection, year):
        self.coding = coding
        self.type = type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.coding, self.type, self.reflection, self.year)

    def is_dynamic(self):
        return self.type == "Dynamic"

