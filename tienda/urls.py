from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path ('ventas/', include('ventas.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
