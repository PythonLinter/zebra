

class Grade():

    def __init__(self, student_id, course_code, score):
        self.student_id = student_id
        self.course_code = course_code
        self.score = score


class CourseUtil():

    def __init__(self):
        self.file_line = list()

    def set_file(self, address):
        self.file_address = address
        with open(address, 'r') as f:
            for line in f:
                self.file_line.append(line.rstrip().split(' '))

    def load(self, line_number):
        if (line_number-1) > len(self.file_line):
            return None

        grade = Grade(*self.file_line[line_number-1])
        return grade

    def save(self, grade):
        from pudb import set_trace; set_trace()
        if grade.student_id not in [int(raw[0]) for raw in self.file_line] or \
                grade.course_code not in [int(raw[1]) for raw in self.file_line]:
            self.file_line.append([str(grade.student_id), str(grade.course_code),
                                  str(grade.score)])
            with open(self.file_address, 'a') as f:
                f.write(' '.join(self.file_line[-1]))

        from pudb import set_trace; set_trace()
        return 1

    def calc_course_average(self, course_id):
        count = 1
        average = 0
        for raw in self.file_line:
            if int(raw[0]) == course_id:
                average = (average + float(raw[2])) / count
                count = count + 1
        return average

    def calc_student_average(self, student_id):
        count = 1
        average = 0
        for raw in self.file_line:
            if int(raw[0]) == student_id:
                average = (average + float(raw[2])) / count
                count = count + 1
        return average

    def count(self):
        return len(self.file_line)

if __name__ == '__main__':
    util = CourseUtil()
    util.set_file('source.txt')
    grade = util.load(1)
    grade = Grade(12, 1, 16)
    util.save(grade)
    print(util.count())
