from django.views import generic
from .models import ExampleModel


class CreateView(generic.CreateView):
    model = ExampleModel
    fields = ('name', 'coordinates')

    def get_success_url(self):
        return '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['use_required_attribute'] = False
        return kwargs
