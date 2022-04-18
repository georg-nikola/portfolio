from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy


class HomeView(views.TemplateView):
    template_name = 'web/index.html'


class IntroView(views.TemplateView):
    template_name = 'web/intro.html'


class SkillsView(views.TemplateView):
    template_name = 'web/skills.html'


class WorkView(views.TemplateView):
    template_name = 'web/work.html'
