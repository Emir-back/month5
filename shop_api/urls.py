from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', home),  # Корневой URL
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/users/', include('users.urls')),

]
