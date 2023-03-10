from circulares import views
from django.urls import path


urlpatterns = [
    path('alls/', views.CircularesView.as_view()),
]
