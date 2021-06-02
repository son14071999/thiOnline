from django.urls import path
from .views import Index
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Home'
urlpatterns = [
    path('', Index.as_view(), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

