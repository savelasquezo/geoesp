from django.urls import path
from .views import Index, Contact, EnvironmentalView, ExplorationView, DesignView

urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('contact', Contact.as_view(), name='Contact'),
    path('info/environmental', EnvironmentalView.as_view(), name='Environmental'),
    path('info/exploration', ExplorationView.as_view(), name='Exploration'),
    path('info/design', DesignView.as_view(), name='Design'),
]