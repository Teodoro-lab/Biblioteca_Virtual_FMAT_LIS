from django import forms


from .models import Comment


class CommentForm(forms.ModelForm):
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
