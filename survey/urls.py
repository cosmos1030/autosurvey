from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.survey_create, name='survey_create'),
    path('<int:survey_id>/', views.survey_detail, name='survey_detail'),
]
