#يكتب في هذا الملف جميع الدوال التي تريد تطبيقها ع جميع ملفات الفيو في الموقع

from .models import Settings



def myfooter(request):
    myfooter = Settings.objects.last()
    return{'myfooter':myfooter}
