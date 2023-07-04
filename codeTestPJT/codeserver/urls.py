from . import views
from django.urls import path

urlpatterns = [
    path('check/', views.check_view )
]
