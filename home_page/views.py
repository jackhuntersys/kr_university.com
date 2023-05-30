from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home_page.html'


class AboutPageView(TemplateView):
    template_name = 'about_page.html'

class BasePageView(TemplateView):
    template_name = 'base.html'


# view.py da oddiy html qaytaradigan oddiy request yaratish pasdagilarni qilamiz
# from django.http import HttpResponse
# def HomePageView(request):
#     return HttpResponse('Hello World')
