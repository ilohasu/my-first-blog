from django.urls import path
from django.views import generic
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('', generic.TemplateView.as_view(template_name='blog/test.html'), name='test'),
]

