from .models import Settings
# from django.views.decorators.cache import cache_page

# @cache_page(60 * 1)
def get_settings(request):
    data = Settings.objects.last()
    return {'settings_data': data}