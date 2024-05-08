from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from library.forms import MaterialUploadForm
from library.models import Course, Resource, Unit
from library.models.material_models import Material
from library.utils import session_visit_register

MATERIALS_TEMPLATE_PATH = "library/material_list.html"

@session_visit_register
class GenericResourceListView(ListView):
    model = Resource
    template_name = MATERIALS_TEMPLATE_PATH

    def setup(self, request, *args, **kwargs):
        print(request.COOKIES)
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        resources = Resource.objects.filter(unit_id=unit.pk, type='Generic')
        return resources
    
    def get_context_data(self, **kwargs):
        path = self.request.path.rstrip('/')  # Ensure no trailing slash
        clean_path = path.rsplit('/', 1)[0]
        context = super().get_context_data(**kwargs)
        context['exercises'] = clean_path + '/exercises'
        context['resources'] = clean_path + '/resources'
        return context

@session_visit_register
class MaterialListView(GenericResourceListView):
    model = Material
    template_name = MATERIALS_TEMPLATE_PATH

    def setup(self, request, *args, **kwargs):
        print(request.COOKIES)
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        materials = Material.objects.filter(unit_id=unit.pk)
        return materials

@session_visit_register
class ExerciseListView(GenericResourceListView):
    model = Resource
    template_name = MATERIALS_TEMPLATE_PATH

    def get_queryset(self):
        course = Course.objects.get(slug=self.kwargs["slug"])
        unit = Unit.objects.get(unit_num=self.kwargs["unit_num"],
                                course_id=course.id)
        exercises = Resource.objects.filter(unit_id=unit.pk, type='Exercise')
        return exercises

class MaterialDetailView(DetailView):
    model = Material
    template_name = MATERIALS_TEMPLATE_PATH

    def get_object(self):
        print('context' )
        material = Material.objects.get(id=self.kwargs['material_id'])
        return material


@session_visit_register
class MaterialUploadFormView(FormView):
    template_name = 'library/upload_form.html'
    form_class = MaterialUploadForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)