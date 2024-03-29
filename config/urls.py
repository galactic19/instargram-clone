
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView, RedirectView
from django_pydenticon.views import image as pydenticon_image


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('instargram.urls')),
    path('', RedirectView.as_view(pattern_name='instargram:post_index'), name='root'),
    path('instartgram/', include('instargram.urls')),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    