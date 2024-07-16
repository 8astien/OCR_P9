from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name = "authentication"

urlpatterns = [
    # path('login/', LoginPageView.as_view(template_name='authentication/login.html'), name='login'),
    path(
        "login/",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,
            next_page=reverse_lazy("feed:home"),
        ),
        name="login",
    ),
    path("signup/", views.signin_view, name="signin"),
    path("logout/", auth_views.LogoutView.as_view(next_page="authentication:login"), name="logout"),
]
