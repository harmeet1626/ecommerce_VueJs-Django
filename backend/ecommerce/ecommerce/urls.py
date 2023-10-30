from django.contrib import admin
from django.urls import path
# from products.views import addProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', addProduct)
]
