from django.urls import path
from django.views import generic
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('', generic.TemplateView.as_view(template_name='blog/test.html'), name='test'),
    path('', views.DiaryList.as_view(), name='list'),
    path('detail/<int:pk>/', views.DiaryDetail.as_view(), name='detail'),
    path('category/<int:pk>/', views.DiaryCategoryList.as_view(), name='category'),
    path('archive/<int:year>/', views.DiaryYearList.as_view(), name='year'),
    path('archive/<int:year>/<int:month>/', views.DiaryMonthList.as_view(), name='month'),
    path('search/', views.DiarySearchList.as_view(), name='search'),
]

