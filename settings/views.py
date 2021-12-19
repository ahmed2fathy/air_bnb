
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import render
from property.models import Property , Place ,Category
# Create your views here.



# الدالة الخاصة بعرض بكل محتويات صفحة الهوم
def home (request):
    places = Place.objects.all().annotate(property_count=Count('property_place')) # كود عرض الاماكن
    category = Category.objects.all() # كود عرض التصنيفات
    restaurant_list= Property.objects.filter(category__name ='Restaurant')[:5]
    hotel_list= Property.objects.filter(category__name ='Hotel')[:5]
    places_list= Property.objects.filter(category__name ='places')[:5]
    
    return render(request, 'settings/home.html' ,{
    'places': places ,
    'category': category,
    'restaurant_list':restaurant_list,
    'hotel_list':hotel_list,
    'places_list':places_list,
    
    })
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