from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
    CommentListView,
    CommentDeleteView,
    accept,
    subscribe,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

    # Bulletin routes
    path('home/<int:pk>/', PostDetailView.as_view(), name='bulletin-detail'),
    path('home/new/', PostCreateView.as_view(), name='bulletin-create'),
    path('home/<int:pk>/update/', PostUpdateView.as_view(), name='bulletin-update'),
    path('home/<int:pk>/delete/', PostDeleteView.as_view(), name='bulletin-delete'),
    path('<int:pk>/subscribe/', subscribe, name='bulletin-subscribe'),

    # Comment routes
    path('home/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('home/comments/', CommentListView.as_view(), name='comment_list'),
    path('home/comments/<int:pk>/accept/', accept, name='comment-accept'),
    path('home/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication routes
    path('accounts/', include('users.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)