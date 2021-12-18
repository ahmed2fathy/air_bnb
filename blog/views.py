from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category

 
class PostList(ListView):
    model     = Post
    paginate_by = 1
    
    
    # دالة البحث
    def get_queryset(self):
        name = self.request.GET.get('q','')
        object_list = Post.objects.filter(
        Q(title__icontains = name) |
        Q(description__icontains = name)
        )
        return object_list
    #------------------------------------------
 
 
class PostDetail(DetailView):
    model = Post
#  الدالة الخاصة بعرض التصنيفات والتاجات والمواضيع المتشابهة في المواضيع او المقالات   ----
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        from taggit.models import Tag
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()
        return context
#   نهاية الدالة الخاصة بعرض التصنيفات والتاجات والمواضيع المتشابهة في المواضيع او المقالات   ---


    # الدالة الخاصة بفلترة التصنيفات
class PostsByCategory(ListView):
    model= Post
    def get_queryset(self):
        slug = self.kwargs ['slug']
        object_list = Post.objects.filter(
        Q(category__name__icontains= slug)
        )
        return object_list
    #-------------------------------------------------------

    
    # الدالة الخاصة بفلترة التاجات
class PostsByTags(ListView):
    model= Post
    def get_queryset(self):
        slug = self.kwargs ['slug']
        object_list = Post.objects.filter(
        Q(tags__name__icontains= slug)
        )
        return object_list
    #-------------------------------------------------------
