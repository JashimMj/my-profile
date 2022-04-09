from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.indexV, name='index'),
    path('about/', views.aboutV, name='about'),
    path('portfolio/', views.portfolioV, name='portfolio'),
    path('contact/', views.contactV, name='contact'),
    path('contact/save/', views.contactsaveV, name='contactsave'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
