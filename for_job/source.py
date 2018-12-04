
class Grade():

    def __init__(self, student_id, course_code, score):
        self.student_id = student_id
        self.course_code = course_code
        self.score = score

    def __eq__(self, other):
        return self.student_id == other.student_id and \
            self.course_code == other.course_code


    def fix_fields(self):
        try:
            self.student_id = int(self.student_id)
            self.course_code = int(self.course_code)
        except(TypeError):
            raise('Student id or course code is not integer')

        try:
            self.score = float(self.score)
        except(TypeError):
            raise('Score is not float')



class CourseUtil():

    def __init__(self):
        self.grades = list()
        self.file_address = None
        self.pre_set_grades = list()

    def set_file(self, address):
        self.grades = []
        self.file_address = address
        with open(address, 'r') as f:
            for line in f:
                grade = Grade(*line.rstrip().split(' '))
                grade.fix_fields()
                if grade not in self.grades:
                    self.grades.append(grade)

        if len(self.pre_set_grades) != 0:
            for element in self.pre_set_grades:
                self.save(element)

    def load(self, line_number):
        if (line_number-1) > len(self.grades):
            return None

        return self.grades[line_number-1]

    def save(self, grade):
        if grade in self.grades:
            return None

        if not self.file_address:
            self.pre_set_grades.append(grade)

        else:
            self.grades.append(grade)
            with open(self.file_address, 'a') as f:
                f.write(' '.join([str(grade.student_id), str(grade.course_code),
                                  str(grade.score), '\n']))


    def calc_course_average(self, course_id):
        count = 0
        grade_sum = 0
        for grade in self.grades:
            if grade.course_code == course_id:
                grade_sum = grade_sum + grade.score
                count = count + 1

        return grade_sum / count

    def calc_student_average(self, student_id):
        count = 0
        grade_sum = 0
        for grade in self.grades:
            if grade.student_id == student_id:
                grade_sum = grade_sum + grade.score
                count = count + 1

        return grade_sum / count

    def count(self):
        return len(self.grades)

if __name__ == '__main__':
    util = CourseUtil()
    grade1 = Grade(1, 1, 12)
    grade2 = Grade(1, 2, 18.5)
    grade3 = Grade(2, 2, 20)
    grade4 = Grade(1, 4, 15)
    grade5 = Grade(3, 1, 20)
    util.save(grade1)
    util.save(grade2)
    util.save(grade3)
    util.save(grade4)
    util.save(grade5)
    util.set_file('source.txt')
