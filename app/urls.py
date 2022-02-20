

from django.urls import path
from .views import home_view,register, special
urlpatterns = [
   path('', home_view, name="home"),
   path('register/',register, name='register'),
   path('special/',special,name='special')
]