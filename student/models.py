from django.db import models

class StudentSemesterProfile(models.Model):
           semester_name= models.CharField(max_length =50)
           semester_short_form = models.CharField(max_length =50)
           def __str__(self):
                return self.semester_name

class StudentProfile(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    gender_choice = (

        ('male', 'Male'),
        ('female', 'Female'),
        ('3rd gender', '3rd Gender')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)

    session = models.CharField(max_length=50)
    #std_semester = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()
    #student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  #foreignkey er karone .roll
'''
semester_choice = (

        ('4-2', '4th year 2nd semester'),
        ('4-1', '4th year 1st semester'),
        ('3-2', '3rd year 1st semester')
        )
        semester = models.CharField(choices=semester_choice, max_length=50)

'''
class Result(models.Model):
       session = models.CharField(max_length=50,unique= True)
       semester = models.CharField(max_length =50)

       roll = models.CharField(max_length=10)
       gpa = models.FloatField()

       def __str__(self):
           return str(self.roll)
unique_together = ['roll', 'semester']
		   
        # semester_choice = (
        #
        #     ('4-2', '4th year 2nd semester'),
        #     ('4-1', '4th year 1st semester'),
        #     ('3-2', '3rd year 1st semester')
        # )
       #semester = models.CharField(choices=semester_choice, max_length=50)



