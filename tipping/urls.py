from django.urls import path, include
from django.views.generic import TemplateView
from .views import refresh_data, create_tips

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('billboard/', TemplateView.as_view(template_name="tipping.html")),
    path('data_refresh/', refresh_data, name='refresh-data'), 
    path('tips/<int:round_id>/', create_tips, name='tips'),
    path('tips/', create_tips, name='tips'),
]