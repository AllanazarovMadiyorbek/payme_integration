from django.urls import path,include


urlpatterns = [
    path('subscribe/',include('subscribe.urls'))
]