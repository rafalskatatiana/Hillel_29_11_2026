# 'Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, avg_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_score = avg_score

    def update_score(self,new_score):
            self.avg_score = new_score
student1 = Student(first_name='Timur', last_name='Black', age=19, avg_score=70)

print("firstname:", student1.first_name,"\nlastname:", student1.last_name, " \nage:", student1.age, "\navg_score:", student1.avg_score)

student1.update_score(88)
print("Новий сeредній бал студента:", student1.avg_score)




