from django.contrib import admin
from  .models import Property , PropertyBook , PropertyImages ,Place, PropertyReview , Category
# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)