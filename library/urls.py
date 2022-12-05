from django.urls import include, path
from .views import (CourseDetailView, CourseListView, ExerciseListView,
                    GenericResourceListView, SemesterListView, CommentFormView,
                    MaterialListView, MaterialDetailView, ContactTemplateView,
                    index_view)

resource_patterns = [
    path("materials", MaterialListView.as_view(), name="material_list"),
    path("resources", GenericResourceListView.as_view(),
         name="resource_list"),
    path("exercises", ExerciseListView.as_view(), name="excercise_list"),
    path("materials/<int:material_id>",
         MaterialDetailView.as_view(),
         name="material_detail"),
    path("resources/<int:material_id>",
         MaterialDetailView.as_view(),
         name="resource_detail"),
    path("exercises/<int:material_id>/",
         MaterialDetailView.as_view(),
         name="exercise_detail"),
]

course_patterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<slug:slug>", CourseDetailView.as_view(), name="course_detail"),
    path("<slug:slug>/unit/<int:unit_num>/", include(resource_patterns)),
]

semester_urls = [
    path("", SemesterListView.as_view(), name="semester_list"),
    path("<int:semester_num>/courses/", include(course_patterns)),
]

urlpatterns = [
    path("", index_view, name="home"),
    path("comments/", CommentFormView.as_view(), name="comment_form"),
    path("contact/", ContactTemplateView.as_view(), name="contact"),
    path("semesters/", include(semester_urls)),
]
