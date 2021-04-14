from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache


# Serve Vue Application
# index_view = never_cache(TemplateView.as_view(template_name='PATH_TO_FRONT_HTML/index.html'))
