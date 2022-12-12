def session_visit_register(target):
    """
    Decorator to register the number of visits to a view
    :param target: class-based view to decorate
    :return: decorated class-based view 

    :description: The decorator will override the setup method of the class-based view
    in order to register the number of visits in the current session.

    :setup: The setup method is called before the dispatch method of the class-based view
    in order to perform some initializations when making a request to the view.

    :model View: https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.View
    """
    parent_setup = target.setup

    def wrapper(self, request, *args, **kwargs):
        visits_info = request.session.get('visits', False)
        current_path = request.path

        if visits_info and visits_info.get(current_path, False):
            current_value = request.session['visits']
            current_value[request.path] = current_value.get(request.path) + 1
            request.session['visits'] = current_value
        elif not visits_info:
            request.session['visits'] = {}
            request.session['visits'][request.path] = 1
        else: # there is a visits_info but not the current_path
            request.session['visits'][request.path] = 1

        parent_setup(self, request, *args, **kwargs)

    target.setup = wrapper
    return target
