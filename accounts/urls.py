from django.urls import path
from django.contrib.auth import views as auth_views
from .views import custom_login_view, custom_logout_view, profile, profile_update_view, register_view

urlpatterns = [
    path("login/", custom_login_view, name="login"),
    path("logout/", custom_logout_view, name="logout"),
    path("signup/", register_view, name="register"),
    path("settings/", profile_update_view, name="profile_update"),
    path("profile/", profile, name="profile"),
    path("password/reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
    path("change-password", auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name="password_change"),
    path("change-password/done", auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"), name="password_change_done"),
]

