
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import render
from property.models import Property , Place ,Category
from blog.models import Post
# Create your views here.



# الدالة الخاصة بعرض بكل محتويات صفحة الهوم
def home (request):
    places = Place.objects.all().annotate(property_count=Count('property_place')) # كود عرض الاماكن
    category = Category.objects.all() # كود عرض التصنيفات
    
    #الاكواد الخاصة بعرض الليستات في الهوم
    resturant_list= Property.objects.filter(category__name ='resturant')[:5]
    hotels_list= Property.objects.filter(category__name ='hotel')[:4]
    places_list= Property.objects.filter(category__name ='places')[:4]
    recent_posts = Post.objects.all()[:4]
   
    # الكود الخاص بعرض العدادت
    user_count = User.objects.all().count()
    resturant_count= Property.objects.filter(category__name ='resturant').count()
    hotels_count= Property.objects.filter(category__name ='hotel').count()
    places_count= Property.objects.filter(category__name ='places').count()
     
     
    return render(request, 'settings/home.html' ,
    {
    'places': places ,
    'category': category,
    'resturant_list':resturant_list,
    'hotels_list':hotels_list,
    'places_list':places_list,
    'recent_posts':recent_posts,
    'user_count':  user_count,
    'resturant_count':resturant_count,
    'hotels_count':hotels_count,
    'places_count':places_count,
    

    }
    )
  #---------------------------------------------  
    
    
    
# الدالة الخاصة بمحرك البحث    
def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')
    
    property_list = Property.objects.filter(
    Q(name__contains= name)&
    Q(place__name__contains= place)
    )
    return render(request, 'settings/home_search.html', {'property_list': property_list})
    #---------------------------------------------

#الدالة الخاصة بعرض صفحة فلتر التصنيفات
def category_filter(request , category):
    category= Category.objects.get(name= category)
    property_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html', {'property_list': property_list})
    
    
#----------------------------------------



def contact_us(request):
    pass