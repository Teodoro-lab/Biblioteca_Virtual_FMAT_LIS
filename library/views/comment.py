from typing import Any
from django.views.generic.edit import FormView

from library.forms import CommentForm
from library.utils import session_visit_register

from accounts.models import CustomUser

@session_visit_register
class CommentFormView(FormView):
    template_name = 'library/comment_form.html'
    form_class = CommentForm
    success_url = '/comments'

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        print(self.request.user.username)
        print (form.instance)
        form.instance.email = CustomUser.objects.get(username=self.request.user.username).email
        form.save()
        return super().form_valid(form)