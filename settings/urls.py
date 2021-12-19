from django.urls import path

from settings.views import home


app_name ='settings'


urlpatterns = [
    path('', home , name ='home'),
]
