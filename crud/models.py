from django.db import models
from django.utils.timezone import now

# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)
    email = models.EmailField(default='example@email.com')
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name + ' ' + self.email

# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()
    
    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)

# Course model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# Lesson
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()
