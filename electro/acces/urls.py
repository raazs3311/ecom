from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='acces'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.base, name = 'base'),
    path('category', views.category, name = 'category'),
    path('product', views.product, name = 'product'),
    path('contact', views.contact, name = 'contact'),
    path('detail<int:id>', views.detail, name= 'detail'),
    path('Buy<int:id>', views.Buy, name= 'Buy'),
    path('search', views.search, name= 'search'),
    
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
