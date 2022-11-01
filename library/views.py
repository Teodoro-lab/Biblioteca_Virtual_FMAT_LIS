from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from .forms import CommentForm
from .models import Course, Material, Semester


def index_view(request):
    buttons = {
        "buttons": ["materials",
                    "examples",
                    "resources"]
    }
    return render(request, 'library/index.html', buttons)

#-------------- Comments -------------

class CommentFormView(FormView):
    template_name = 'library/comment_form.html'
    form_class = CommentForm
    success_url = '/'

#-------------- Materials -------------

class MaterialListView(ListView):
    model = Material
    template_name = "material_list.html"
    
    def get_queryset(self):
        course = Course.objects.filter(
            slug=self.kwargs["slug"]
        ).first()
        
        return Material.objects.filter(
            course=course.id
        )
    
    
#-------------- Semesters -------------

class SemesterListView(ListView):
    model = Semester
    template_name = "semester_list.html"
        

#-------------- Courses -------------

class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
    
    def get_queryset(self):
        return Course.objects.filter(
            semester=self.kwargs['semester_num']
        )


class CourseDetailView(DetailView):
    model = Course
    template_name = "library/course_detail.html"
    
#
def pdf_view(request, pdf_path):
    try:
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')
