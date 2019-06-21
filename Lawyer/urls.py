from django.urls import path
from Lawyer import views

urlpatterns = [
    path('tutorial', views.Tutorial.as_view()),
    path('validation', views.ValidationView.as_view()),
    path('informations', views.LawyersView.as_view()),
    path('detail/<id>', views.LawyerDetailView.as_view()),
    path('generic-informations', views.GenericLawyersView.as_view()),
    path('generic-detail/<pk>', views.GenericLawyerDetailView.as_view()), 
]