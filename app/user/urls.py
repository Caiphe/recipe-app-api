from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('creat/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreatTokenView.as_view(), name='token'),
    path('me/', views.ManageUserVIew.as_view(), name='me'),
]