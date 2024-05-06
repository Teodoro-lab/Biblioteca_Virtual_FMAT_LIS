import magic
from django import forms
from django.utils import timezone

from .models import Comment, Resource

MAX_UPLOAD_SIZE = 1024*1024*2
ACCEPTABLE_MIME_TYPES = ['application/pdf', 'image/jpeg', 'image/png', 'image/gif']

class ResetMixin:
    @staticmethod
    def last_reset_was_24_hours_ago(last_reset):
        today_minus_24 = timezone.now() - timezone.timedelta(days=1)
        return last_reset < today_minus_24


class BaseUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def validate_quota(self, quota_field):
        """
        Validates the quota field of the user. If the user has remaining quota, it decrements it by 1.
        If the user has no remaining quota, it resets the quota if the last reset was 24 hours ago.
        If the last reset was not 24 hours ago, it adds an error to the form field.
        """
        user = self.request.user
        remaining_quota = getattr(user, quota_field)

        if remaining_quota > 0:
            setattr(user, quota_field, remaining_quota - 1)
            user.save()
        elif ResetMixin.last_reset_was_24_hours_ago(user.last_reset):
            user.reset_form_quota()
            remaining_quota = getattr(user, quota_field)
            setattr(user, quota_field, remaining_quota - 1)
            user.save()
        else:
            error_field =  self.Meta.quota_mappings.get(quota_field)
            error_msg = self.Meta.quota_error_msg.get(quota_field)
            self.add_error(error_field, error_msg)

class CommentForm(BaseUserForm, ResetMixin):
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
        labels = {'comment': 'Comentario'}
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'texto-formulario cuadros'}),
        }
        # Map the quota field to the form field to add the error message
        quota_mappings = {'comment_quota': 'comment'}
        # Map the quota field to error message to display when the quota is exceeded
        quota_error_msg = {'comment_quota': 'No puedes comentar más hoy!'}

    def clean(self):
        cleaned_data = super().clean()
        self.validate_quota('comment_quota')
        return cleaned_data 


class MaterialUploadForm(BaseUserForm, ResetMixin):
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
        # Map the quota field to the form field to add the error message
        quota_mappings = {'file_quota': 'upload'}
        # Map the quota field to the form field to add the error message
        quota_error_msg = {'file_quota': 'No puedes crear más archivos hoy'}
        
    def clean(self):
        cleaned_data = super().clean()
        self.validate_quota('file_quota')
        return cleaned_data

    def clean_upload(self):
        """
        Validates the uploaded file. 
        The file should not exceed 2MB and should be either a PDF or an image (JPEG, PNG, or GIF).
        """
        cleaned_data = super().clean()
        upload = cleaned_data.get('upload')
    
        if upload:
            myFile = upload.open()
            mime = magic.from_buffer(myFile.read(2048), mime=True)

            if upload.size > MAX_UPLOAD_SIZE:
                self.add_error('upload', 'El archivo es demasiado grande')
            elif mime not in ACCEPTABLE_MIME_TYPES:
                self.add_error('upload', 'El archivo no es un PDF o una imagen')

        return upload
