from django import forms

from .models import Comment, Resource


class CommentForm(forms.ModelForm):
    """
    Form for the Comment model related to:
    models:
        :model:`library.Material`.
    view:
        :view:`library.views.CommentFormView`.
    """
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment': 'Comentario',  
        }
        widgets = {
            'comment':
            forms.Textarea(attrs={
                'class': 'texto-formulario cuadros',
            }),
        }


class MaterialUploadForm(forms.ModelForm):
    """
    Form for the Comment model related to:
    models:
        :model:`library.Material`.
    view:
        :view:`library.views.CommentFormView`.
    """

    class Meta:
        model = Resource
        fields = '__all__'

    