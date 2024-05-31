from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('computer_api.computers.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
