from django.urls import path
from .views import contact, contact_success

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]