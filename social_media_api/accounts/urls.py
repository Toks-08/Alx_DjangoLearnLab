from .views import RegisterView, LoginView, ProfileView, UpdateProfileView
from django.urls  import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view(), name= 'profile-view'),
    path('profile/update/', UpdateProfileView.as_view(), name= 'profile-update')

]