from django.contrib import admin

from .models import (Career, Comment, Course, Material, Resource, Semester,
                     Unit, visit_statistics)

admin.site.register(Semester)
admin.site.register(Career)
admin.site.register(Course)
admin.site.register(Material)
admin.site.register(Comment)
admin.site.register(Unit)
admin.site.register(Resource)
admin.site.register(visit_statistics)
