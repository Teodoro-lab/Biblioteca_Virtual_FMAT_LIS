from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import CommentForm
from .models import Course, Material, Semester, Unit, Resource


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
    template_name = "library/material_list.html"

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.filter(unit_num=self.kwargs["unit_num"],
                                   course_id=course.id).first()
        materials = Resource.objects.filter(unit_id=unit.pk, type='Exercise')
        return materials


class ExcersiseListView(ListView):
    model = Resource
    template_name = "library/material_list.html"

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.filter(unit_num=self.kwargs["unit_num"], course_id=course.id).first()
        exercises = Resource.objects.filter(unit_id=unit.pk, type='Exercise')
        return exercises


class GenericResourceListView(ListView):
    model = Resource
    template_name = "library/material_list.html"

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.filter(unit_num=self.kwargs["unit_num"],
                                   course_id=course.id).first()
        resources = Resource.objects.filter(unit_id=unit.pk, type='Generic')
        return resources


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
    extra_context = {'units': Unit.objects.filter}

    def get_object(self):
        course = Course.objects.get(slug=self.kwargs['slug'])
        return course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['units'] = Unit.objects.filter(course=self.get_object().id)
        context['links'] = [("Materiales", "materials"),
                            ("Ejercicios", "exercises"),
                            ("Recursos", "resources")]
        return context


class MaterialDetailView(DetailView):
    model = Material
    template_name = "library/material_detail.html"

    def get_object(self):
        material = Material.objects.filter(
            id=self.kwargs['material_id']).first()
        return material