from django.urls import path
from .views import redmiallviews, redmidetailviews, iphoneallviews, iphonedetailviews


urlpatterns = [
    path('redmi/all/', redmiallviews),
    path('redmi/details/<str:tel_model>', redmidetailviews),
    path('iphone/details/<int:tel_id>', iphonedetailviews),
    path('iphone/all/',iphoneallviews)
]