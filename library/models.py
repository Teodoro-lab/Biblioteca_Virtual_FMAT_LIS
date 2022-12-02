from django.db import models
from django.urls import reverse


class Career(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Semester(models.Model):
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    semester_number = models.DecimalField(primary_key=True,max_digits=14, decimal_places=0)

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
        return reverse("course_detail", kwargs={"semester_num":self.semester, "slug": self.slug})


class Material(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_publisehd = models.DateTimeField('date published')
    title = models.CharField(max_length=120)
    description = models.TextField()
    upload = models.FileField(default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    email = models.EmailField()
    comment = models.TextField()

    def save(self):
        print("Saving comment")
        return super().save()
    
