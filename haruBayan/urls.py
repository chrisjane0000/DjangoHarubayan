from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("myapp.urls", "myapp"), namespace="myapp")),  # Correct namespace to avoid any conflicts
]
