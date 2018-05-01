from django.urls import path

from . import views

app_name = 'dbconect'
urlpatterns = [
    # ex: /dbconect/
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
    # ex: /dbconect/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /dbconect/2/sequence/
    path('<int:sequencing_id>/sequence/', views.sequence, name='sequence')
]
