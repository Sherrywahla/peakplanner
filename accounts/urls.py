from django.urls import path
from django.contrib.auth import views as auth_views
from .views import custom_login_view, custom_logout_view, profile, profile_update_view, register_view

urlpatterns = [
    path("login/", custom_login_view, name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_update_view, name="profile_update"),
    path("profile/", profile, name="profile"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]

