from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy


class HomeView(views.TemplateView):
    template_name = 'web/index.html'


class AboutView(views.TemplateView):
    template_name = 'web/about.html'


class ProjectsView(views.TemplateView):
    template_name = 'web/projects.html'


class ContactView(views.TemplateView):
    template_name = 'web/contact.html'
