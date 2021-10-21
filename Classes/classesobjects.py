class Student:
    # initialize function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def fail_class(self):
        # gpa drops
        self.gpa -= 1

        self.gpa = max(self.gpa, 1)

        # if gpa falls under 2, then you will be on probation
        if self.gpa < 2:
            self.is_on_probation = True

    def pass_class(self):
        self.gpa += 1

        self.gpa = min(self.gpa, 4)

        if self.gpa > 2:
            self.is_on_probation = False

    # make a string value
    def __repr__(self):
        string_value = f"{self.name} (Major: {self.major}; GPA: {self.gpa}; On Probation: {self.is_on_probation})"

        return string_value
