from django.urls import path
from .views import Login, Signup, Ajax
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myuser'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('ajax/', Ajax.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
