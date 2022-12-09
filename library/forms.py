from django import forms

from .models import Comment


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
        fields = ['email', 'comment']

        widgets = {
            'email':
            forms.TextInput(attrs={
                'class': 'texto-formulario cuadros',
            }),
            'comment':
            forms.Textarea(attrs={
                'class': 'texto-formulario cuadros',
            }),
        }
