from django.urls import path
from .views import contact, contact_success, contact_admin

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('admin/contact/', contact_admin, name='contact_admin'),
]
