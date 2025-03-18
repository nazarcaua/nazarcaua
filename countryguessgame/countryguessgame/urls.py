from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, login, register, styles

urlpatterns = [
    path('', home, name='index'),          # Home page
    path('login/', login, name='login'),    # Login page
    path('register/', register, name='register'),  # Register page
    path('styles/', styles, name='styles'),  # Styles endpoint (if needed)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
