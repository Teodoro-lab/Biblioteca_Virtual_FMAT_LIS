from django.urls import path, re_path
from .views import (
    CourseDetailView,
    CourseListView,
    SemesterListView,
    CommentFormView,
    MaterialListView,
    index_view, pdf_view
)

urlpatterns = [
    path("", index_view, name="home"),
    
    path("comments/", 
         CommentFormView.as_view(), name="comment_list"),

    path("semesters/", 
         SemesterListView.as_view(), name="semester_list"),

    path("semesters/<int:semester_num>/courses",
         CourseListView.as_view(), name="course_list"),
    
    path("semesters/<int:semester_num>/courses/<slug:slug>",
         CourseDetailView.as_view(), name="course_detail"),

    path("semesters/<int:semester_num>/courses/<slug:slug>/materials", 
         MaterialListView.as_view(), name="material_list"),
    path('pdf/<str:pdf_name>', pdf_view, name='pdf')

]
