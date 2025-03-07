from django.urls import path
from .views import (
    IssueListCreateView, IssueDetailView, CommentListCreateView,
    NotificationListView, MarkNotificationReadView, RegisterView,
    LoginView, UserView, api_root
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserView.as_view(), name='user'),
    path('issues/', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),
    path('issues/<int:issue_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/mark-read/', MarkNotificationReadView.as_view(), name='mark-notification-read'),
]

