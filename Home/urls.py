from django.urls import path
from .views import Index, Contact

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('contact', Contact.as_view(), name='Contact'),
]