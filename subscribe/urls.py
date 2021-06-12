from django.urls import path
from .views import CardCreateApiView,CardVerifyApiView ,PaymentApiView

urlpatterns = [
    path('card/create/', CardCreateApiView.as_view(), name="card-create"),
    path('card/verify/', CardVerifyApiView.as_view(), name='card-verify'),
    path('payment/', PaymentApiView.as_view(), name='payment'),
]