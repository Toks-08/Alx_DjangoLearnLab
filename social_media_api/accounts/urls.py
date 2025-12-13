from .views import RegisterView, LoginView, ProfileView, UpdateProfileView, FollowUserView, UnfollowUserView
from . import views
from django.urls  import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view(), name= 'profile-view'),
    path('profile/update/', UpdateProfileView.as_view(), name= 'profile-update'),
    path('follow/<int:user_id>/',FollowUserView.as_view(), name = 'follow-user' ),
    path('unfollow/<int:user_id>/',UnfollowUserView.as_view(), name = 'unfollow-user' )


]