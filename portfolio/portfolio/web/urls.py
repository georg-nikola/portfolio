from django.urls import path

from portfolio.web.views import HomeView, AboutView, ProjectsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
)