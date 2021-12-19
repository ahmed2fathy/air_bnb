from django.urls import path

from settings.views import home, home_search ,category_filter


app_name ='settings'


urlpatterns = [
    path('', home , name ='home'),
    path('search' , home_search , name= 'home_search'),
    path('category/<slug:category>' , category_filter , name= 'category_filter'),
    
    
]  

