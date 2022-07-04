from django.urls import path

from users.views import Profile, istek

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('istek/', istek, name='istek')

]
