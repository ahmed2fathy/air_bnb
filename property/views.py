from typing import Reversible
from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
from django.contrib import messages
from .filters import PropertyFilter
from django_filters.views import FilterView

# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 1   #لتحديد عدد المواضيع المراد ظهورها في كل صفحة
    filterset_class = PropertyFilter
    template_name = 'property\property_list.html'
    ##filter
    ##pagnation
    
class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm
    #book
    
    #  الدالة الخاصة بعرض المواضيع او المقالات المتشابهة حسب التصنيف-----
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    #  نهايةالدالة الخاصة بعرض المواضيع او المقالات المتشابهة----------------
    
    
    
# الكود الخاص بفورم الحجز
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ') ### send gmail message
            return redirect('/')
            #  نهاية الكود الخاص بفورم الحجز
           

   
            
 
    
