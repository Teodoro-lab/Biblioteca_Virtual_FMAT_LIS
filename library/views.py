from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import CommentForm
from .models import Course, Material, Semester


def index_view(request):
    return render(request, 'library/index.html')


#-------------- utils -------------

class ContactTemplateView(TemplateView):
    template_name = 'library/contact.html'

class CommentFormView(FormView):
    template_name = 'library/comment_form.html'
    form_class = CommentForm
    success_url = '/comments'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


#-------------- Materials -------------


class MaterialListView(ListView):
    model = Material
    template_name = "material_list.html"

    def get_queryset(self):
        course = Course.objects.filter(slug=self.kwargs["slug"]).first()

        return Material.objects.filter(course=course.id)


#-------------- Semesters -------------


class SemesterListView(ListView):
    model = Semester
    template_name = "semester_list.html"

    def get_queryset(self):
        return Semester.objects.all()


#-------------- Courses -------------


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

    def get_queryset(self):
        return Course.objects.filter(semester=self.kwargs['semester_num'])


class CourseDetailView(DetailView):
    model = Course
    template_name = "library/course_detail.html"


#-------------- pdf -------------


def pdf_view(request, pdf_path):
    try:
        return FileResponse(open(pdf_path, 'rb'),
                            content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')
