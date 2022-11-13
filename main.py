class Student:
    students_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = []
        Student.students_list.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer)\
                and course in [lecturer.courses_attached, self.courses_in_progress]:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        self.average_rating = round(sum(self.grades.values()) / len(self.grades.values()), 2)
        if not isinstance(other, Student):
            print('Не является Студентом')
            return
        return self.average_rating < other.average_rating

    def _average_rating_(self):
        if not self.grades:
            return 'Ошибка'
        else:
            for grades in self.grades.values():
                if grades is float:
                    self.average_rating = + grades
                elif grades is list:
                    self.average_rating.append(grades)
            self.average_rating = round(sum(grades) / len(grades), 2)
            return print(f'Средняя оценка за домашние задания: {self.average_rating}')

    def __str__(self):
        def _average_rating_():
            if not self.grades:
                return 'Ошибка'
            else:
                for grades in self.grades.values():
                    self.average_rating.append(grades)
                self.average_rating = round(sum(grades) / len(grades), 2)
                return self.average_rating
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {_average_rating_()}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    lecturers_list = []

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.grades = {}
        self.average_rating = []
        Lecturer.lecturers_list.append(self)

    def _average_rating_(self):
        if not self.grades:
            return 'Ошибка'
        else:
            for grades in self.grades.values():
                if grades is float:
                    self.average_rating = + grades
                elif grades is list:
                    self.average_rating.append(grades)
            self.average_rating = round(sum(grades) / len(grades), 2)
            return print(f'Средняя оценка за лекции: {self.average_rating}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является Лектором')
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        def average_rating():
            if not self.grades:
                return 'Ошибка'
            else:
                for grades in self.grades.values():
                    self.average_rating.append(grades)
                self.average_rating = round(sum(grades) / len(grades), 2)
                return self.average_rating
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating()}'
        return res


class Reviewer (Mentor):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_grade_hw(course):
    average_score_hw = []
    for student in Student.students_list:
        if course in student.finished_courses:
            for grades in student.grades.get(course):
                average_score_hw.append(grades)
    average_score_hw = round(sum(average_score_hw) / len(average_score_hw), 2)
    res = f'Средняя оценка по курсу {course} среди студентов : {average_score_hw}'
    return print(res)


def average_grade_lect(course):
    average_score_lect = []
    for lecturer in Lecturer.lecturers_list:
        if course in lecturer.courses_attached:
            for grades in lecturer.grades.get(course):
                average_score_lect.append(grades)
    average_score_lect = round(sum(average_score_lect) / len(average_score_lect), 2)
    res = f'Средняя оценка по курсу {course} среди лекторов: {average_score_lect}'
    return print(res)


Ilya = Student("Илья", "Карьялайнен", "муж.", )
Sasha = Student('Александра', 'Денисова', 'жен.')
Oleg = Lecturer('Олег', 'Андреев', 'муж.')
Nikita = Lecturer('Никита', 'Количенков', 'муж.')
Anna = Reviewer('Анна', 'Феоктистова', 'жен.')
Misha = Reviewer('Михаил', 'Якубов', 'муж.')

Ilya.finished_courses = ['Python', 'Git', 'PyCharm', 'Discord']
Ilya.courses_in_progress = ['React']
Ilya.grades = {'Python': [10], 'Git': [9]}

Sasha.finished_courses = ['Python', 'PyCharm', 'PHP', 'C#', 'Java']
Sasha.courses_in_progress = ['Discord']
Sasha.grades = {'Python': [10], 'PyCharm': [8]}

Oleg.courses_attached = ['Python', 'Git', 'React', 'PHP', 'PyCharm', 'Discord']
Oleg.grades = {'Python': [10], 'PHP': [9], 'React': [10]}

Nikita.courses_attached = ['Python', 'Git', 'React', 'PHP', 'PyCharm', 'Discord', 'Java']
Nikita.grades = {'Python': [9], 'Git': [10], 'React': [8]}

Anna.courses_attached = ['Python', 'Git', 'React', 'PHP', 'C#', 'Java']
Anna.grades = {'Python': [9], 'Git': [10], 'React': [9]}

Misha.courses_attached = ['Python', 'Git', 'React', 'Ruby', 'C#', 'Java']
Misha.grades = {'C#': [9], 'Java': [10], 'React': [9]}

Ilya.rate_lecturer(Oleg, 'PyCharm', 10)
Ilya.rate_lecturer(Nikita, 'Discord', 8)

Sasha.rate_lecturer(Oleg, 'C#', 9)
Sasha.rate_lecturer(Nikita, 'Java', 9)

Anna.rate_hw(Ilya, 'Python', 10)
Anna.rate_hw(Sasha, 'Python', 9)

Misha.rate_hw(Sasha, 'PyCharm', 9)
Misha.rate_hw(Ilya, 'Git', 8)

print(Ilya)
print(Sasha)
print(Oleg)
print(Nikita)
print(Anna)
print(Misha)

print(Ilya.grades)
print(Sasha.grades)
Ilya._average_rating_()
Sasha._average_rating_()
print(Ilya.average_rating < Sasha.average_rating)
Oleg._average_rating_()
Nikita._average_rating_()
print(Oleg.average_rating < Nikita.average_rating)
average_grade_hw('Python')
average_grade_lect('React')
