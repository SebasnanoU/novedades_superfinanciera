from novedades import views
from django.urls import path


urlpatterns = [
    path('alls/', views.NovedadesView.as_view()),
]
