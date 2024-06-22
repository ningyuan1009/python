
from django.urls import path,re_path
from . import views
from .views import ProtectedView
urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
]
