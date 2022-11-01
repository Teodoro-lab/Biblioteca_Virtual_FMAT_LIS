from django.contrib import admin

from .models import Semester, Career, Course, Material, Comment

admin.site.register(Semester)
admin.site.register(Career)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Comment)
