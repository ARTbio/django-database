from django.urls import path

from . import views

app_name = 'drosobase'
urlpatterns = [
    # ex: /drosobase/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /drosobase/2/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /drosobase/searchstocks/
    path('searchstocks/', views.searchstock, name='searchstocks'),
    # ex: /drosobase/Flybase/
    path('Flybase/', views.FlybaseIndexView.as_view(), name='FB_index'),
   # ex: /drosobase/Flybase/2/
    path('Flybase/<int:pk>/', views.FlybaseDetailView.as_view(), name='flybase_detail')
]
