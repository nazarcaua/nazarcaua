from django.urls import path
from countryguessgame.views import guess_country

urlpatterns = [
    path('guess/', guess_country, name='guess_country'),
]