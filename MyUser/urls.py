from django.urls import path
from .views import Login, Signup, Ajax, Info, Logout, forgotpass
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myuser'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('info/', Info.as_view(), name='info'),
    path('forgotpass', forgotpass, name='forgot'),
    path('logout', Logout.as_view(), name='logout'),

    path('ajax/', Ajax.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
