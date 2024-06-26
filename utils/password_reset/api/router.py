from django.urls import path
from .views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]