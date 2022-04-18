from django.urls import path

from portfolio.web.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('intro/', HomeView.as_view(), name='intro'),
    path('skills/', HomeView.as_view(), name='skills'),
    path('work/', HomeView.as_view(), name='work'),
)