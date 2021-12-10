from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('computers/', include('computers_and_accessories.category.computer.urls', namespace='computers')),
]
