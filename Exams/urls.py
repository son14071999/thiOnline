from django.urls import path
from .views import create_exam, takeTheExams, ListExams, checkAnswers, Manage
from django.conf import settings
from django.conf.urls.static import static

app_name = 'exam'
urlpatterns = [
    path('create/', create_exam.as_view(), name='create-exam'),
    path('list/', ListExams.as_view(), name='show-list-exam'),
    path('do/<str:nameExam>/', takeTheExams.as_view(), name='do-exam'),
    path('do/score', checkAnswers.as_view(),name='check'),
    path('manageExams/', Manage.as_view(), name='manage' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

