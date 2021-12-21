from django.shortcuts import render
from django.views.generic import ListView

from .models import About ,FAQ
# Create your views here.




class  AboutView(ListView):
    model = FAQ
    
    
    # الدالة الخاصة بعرض تابات about
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context
    
    
    
    

    
    
    


