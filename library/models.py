from django.db import models
from django.urls import reverse


class Career(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Semester(models.Model):
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    semester_number = models.DecimalField(primary_key=True,
                                          max_digits=14,
                                          decimal_places=0)

    def __str__(self):
        return str(self.semester_number)


class Course(models.Model):
    name = models.CharField(max_length=120)
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT)
    description = models.TextField(default="Enjoy the course")
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course_detail",
                       kwargs={
                           "semester_num": self.semester,
                           "slug": self.slug
                       })


class Unit(models.Model):
    name = models.CharField(max_length=120)
    course = models.OneToOneField(Course,
                                         on_delete=models.CASCADE,
                                         primary_key=True)
    description = models.TextField(default="Enjoy the unit")
    unit_num = models.DecimalField(max_digits=14, decimal_places=0)


class Material(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date_publisehd = models.DateTimeField('date published')
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class Resource(Material):
    types = [
        ('Generic', 'Generic'),
        ('Excerise', 'Excerise'),
    ]

    upload = models.FileField(default=None)
    type = models.CharField(max_length=10, choices=types, default='Generic')

    def __str__(self):
        return super().title


class Comment(models.Model):
    email = models.EmailField()
    comment = models.TextField()