from django.contrib import admin
from .models import Base, Category, Contact, Dis, Product, logo, order ,order, paralex

# Register your models here.

admin.site.register(Base)
admin.site.register(order)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Dis)
admin.site.register(logo)
admin.site.register(paralex)
# admin.site.register(logo)

