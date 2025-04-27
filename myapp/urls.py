from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import authView, home, menu_categories  # Import views correctly
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),  # Login page as root
    path("home/", home, name="home"),  # Home page, requires login
    path("signup/", authView, name="authView"),  # Signup page
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth system
    path("menu-categories/", menu_categories, name="menu_categories"),  # Menu categories
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)