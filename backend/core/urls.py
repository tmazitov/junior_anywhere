from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Импорт функций из пользовательских обработчиков
from users_app.user_handlers.user_register import register as user_register_view
from users_app.user_handlers.user_profile import profile as user_profile_view
from users_app.user_handlers.user_auth import test_authentication as test_auth_view
from users_app.forms import UserLoginForm
from . import views
from users_app.user_handlers.get_user import get_user_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_register_view, name='register'),
    path('profile/', user_profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('test-auth/', test_auth_view, name='test_auth'),
    path('user/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
