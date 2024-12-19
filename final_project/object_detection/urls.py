from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from users.views import *
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', get_dashboard, name='dashboard'),
    path('dashboard/add_object/', add_object, name='add_object'),
    path('process/<int:image_id>/', process_image_feed, name='process_image'),
    path('delete_image/<int:image_id>/', delete, name='delete_image'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('about_user/', get_user_info, name='about_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
