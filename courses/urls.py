from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView,AboutView,ContactView,CourseListView, CourseDetailView,LessonDetailView, SearchView, olusturmak_klase, olusturmak_lende, olusturmak_mesim

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:category>/', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', SearchView, name='kerko_kurs'),
    path('olusturmak/klase', olusturmak_klase, name='olusturmak_klase'),
    path('olusturmak/lende', olusturmak_lende, name='olusturmak_lende'),
    path('olusturmak/mesim', olusturmak_mesim, name='olusturmak_mesim')
]
