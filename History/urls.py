from django.urls import path
from .views import HistoryView, View_exam

app_name = 'history'
urlpatterns = [
    path('', HistoryView.as_view(), name='getHistory'),
    path('history/<id_history>/', View_exam.as_view(), name='show_history')
]