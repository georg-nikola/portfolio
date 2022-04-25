from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'web/index.html'


class AboutView(views.TemplateView):
    template_name = 'web/about.html'


class ProjectsView(views.TemplateView):
    template_name = 'web/projects.html'
