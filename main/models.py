from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    age = models.IntegerField()
    subject = models.CharField(max_length=30)

    # Use related_name to prevent reverse access clashes
    groups = models.ManyToManyField(
        'auth.Group', related_name='main_user_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='main_user_permissions_set', blank=True
    )

    def __str__(self):
        return self.username
    
    
# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    program_of_study = models.CharField(max_length=100)
    graduation_year = models.IntegerField()

# Faculty Model
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    department = models.CharField(max_length=100)
    office_number = models.CharField(max_length=20)

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in months
    start_date = models.DateField()
    faculty = models.ManyToManyField(Faculty, related_name='courses')

# Job Placement Model
class JobPlacement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='job_placements')
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    date_placed = models.DateField()

# Testimonial Model
class Testimonial(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='testimonials')
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Inquiry Model
class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.user.username}"
