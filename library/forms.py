from django import forms

from .models import Comment, Resource
import magic

MAX_UPLOAD_SIZE = 1024*1024*2
ACCEPTABLE_MIME_TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'image/gif']

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
    def clean_upload(self):
        """
        Validates the uploaded file. 
        The file should not exceed 2MB and should be either a PDF or an image (JPEG, PNG, or GIF).
        """
        cleaned_data = super().clean()
        upload = cleaned_data.get('upload')
    
        if upload:
            myFile = upload.open()
            mime = magic.from_buffer(myFile.read(2048, mime=True))
    
            if upload.size > MAX_UPLOAD_SIZE:
                self.add_error('upload', 'El archivo es demasiado grande')
            elif mime not in ACCEPTABLE_MIME_TYPES:
                self.add_error('upload', 'El archivo no es un PDF o una imagen')
        return cleaned_data

    