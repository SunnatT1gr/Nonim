from django.urls import path
from .views import homeview, ContactView, AboutView, TestView, FruitView

app_name = 'core'
urlpatterns = [
    path('', homeview, name="home_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('fruit/', FruitView.as_view(), name="fruit_page"),
    path('test/', TestView.as_view(), name="test_page")
]