from django.urls import path
from Lawyer import views

urlpatterns = [
    path('tutorial', views.Tutorial.as_view()),
    path('validation', views.ValidationView.as_view()),
    path('informations', views.LawyersView.as_view()),
]