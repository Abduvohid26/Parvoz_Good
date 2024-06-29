from django.urls import path
from .views import Register, Login, Loguot, Profile, ProfileEdit

app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Loguot.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile-edit/', ProfileEdit.as_view(), name='profile-edit')

]