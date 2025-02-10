from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Default view for the root URL
def home_view(request):
    return JsonResponse({"message": "Welcome to the Academic Issue Tracking API!"})

urlpatterns = [
    path('', home_view),  # Redirects '/' to a simple API message
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
