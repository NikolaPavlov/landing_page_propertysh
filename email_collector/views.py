from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import SubscribeForm


class HomePageView(CreateView):
    form_class = SubscribeForm
    template_name = 'index.html'
    success_url = reverse_lazy('success')


def success_view(request):
    return render(request, 'success.html', {})
