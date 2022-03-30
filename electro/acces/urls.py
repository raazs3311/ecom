from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='acces'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.base, name = 'base'),
    path('base', views.base, name = 'base'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('Sign', views.Sign, name = 'Sign'),
    path('category', views.category, name = 'category'),
    path('product', views.product, name = 'product'),
    path('contact', views.contact, name = 'contact'),
    path('detail<int:id>', views.detail, name= 'detail'),
    path('Buy<int:id>', views.Buy, name= 'Buy'),
    path('search', views.search, name= 'search'),
    path('Sign', views.Sign, name= 'Sign'),
    
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
