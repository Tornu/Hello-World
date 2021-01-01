from django.urls import path
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html')),
    path('project',TemplateView.as_view(template_name='project.html'))
]