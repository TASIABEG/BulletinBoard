from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    # password reset route
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),

    # password reset is done successfully
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),

    # password reset confirmation
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# authentification/authorization by allauth
urlpatterns += [
    path('accounts/', include('allauth.urls'))
    ]