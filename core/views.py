from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class TestView(TemplateView):
    template_name = 'testimonial.html'
    
class FruitView(TemplateView):
    template_name = 'fruit.html'

# Create your views here.
