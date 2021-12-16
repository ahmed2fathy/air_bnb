from django.contrib import admin
from  .models import Property ,  PropertyImages ,Place, PropertyReview , Category,PropertyBook




# summernote الكود الخاص بمكتبة المحرر -------------------
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
# summernote  نهاية الكود الخاص بمكتبة المحرر -------------------



# Register your models here.
admin.site.register(Property , SomeModelAdmin )
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)