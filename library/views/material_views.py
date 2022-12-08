from django.views.generic import DetailView, ListView

from library.models import Course, Resource, Unit
from library.models.material_models import Material
from library.utils import session_visit_register

MATERIALS_TEMPLATE_PATH = "library/material_list.html"


@session_visit_register
class MaterialListView(ListView):
    model = Material
    template_name = MATERIALS_TEMPLATE_PATH

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        materials = Material.objects.filter(unit_id=unit.pk)
        return materials


@session_visit_register
class ExerciseListView(ListView):
    model = Resource
    template_name = MATERIALS_TEMPLATE_PATH

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        exercises = Resource.objects.filter(unit_id=unit.pk, type='Exercise')
        return exercises


@session_visit_register
class GenericResourceListView(ListView):
    model = Resource
    template_name = MATERIALS_TEMPLATE_PATH

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        resources = Resource.objects.filter(unit_id=unit.pk, type='Generic')
        return resources



class MaterialDetailView(DetailView):
    model = Material
    template_name = MATERIALS_TEMPLATE_PATH

    def get_object(self):
        material = Material.objects.get(id=self.kwargs['material_id'])
        return material