from django.urls import path

from . import views

app_name = 'drosobase'
urlpatterns = [
    # ex: /drosobase/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /drosobase/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('searchstocks/', views.searchstock, name='searchstocks')
]
