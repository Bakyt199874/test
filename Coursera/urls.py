"""Coursera URL конфигурациясы

`urlpatterns` тизмеси URL'дерди көрүүлөргө багыттайт. Көбүрөөк маалымат алуу үчүн караңыз:
     https://docs.djangoproject.com/en/2.1/topics/http/urls/
Мисалдар:
Функция көрүнүштөрү
     1. Импортту кошуңуз: my_app импорттоо көрүнүштөрүнөн
     2. URL үлгүлөрүнө URL кошуңуз: path('', views.home, name='home')
Класстык көз караштар
     1. Импорт кошуңуз: from other_app.views import Home
     2. URL үлгүлөрүнө URL кошуңуз: path('', Home.as_view(), name='home')
Анын ичинде башка URLconf
     1. include() функциясын импорттоо: django.urls'тен import include, path
     2. URL үлгүлөрүнө URL кошуңуз: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500

handler404 = 'courses.views.view_404'
handler500 = 'courses.views.view_500'
handler403 = 'courses.views.view_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls',namespace='courses')),
    path('', include('blog.urls',namespace='blogs')),
    path('', include('memberships.urls',namespace='memberships')),
    path('', include('users.urls',namespace='users')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
