from .models import Settings
#from django.views.decorators.cache import cache_page
from django.core.cache import caches


# def get_settings(request):
#     data = Settings.objects.last()
#     return {'settings_data':data}

#@cache_page(60 * 1)
def get_settings(request):
    #cHECK DATA IN CASH
    settings_data = caches['default'].get('settings_data')  
    print('old data cache')
    if not settings_data:
        settings_data = Settings.objects.last()
        print('new cache')
        caches['default'].set('settings_data', settings_data, timeout=60 * 1)
    return {'settings_data': settings_data}



# def get_expensive_queryset():
#     queryset = cache.get('expensive_queryset')
#     if not queryset:
#         queryset = MyModel.objects.filter(...)
#         cache.set('expensive_queryset', queryset, timeout=60*15)
#     return queryset
