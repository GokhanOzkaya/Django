from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home",views.home),
    path("furnitures",views.furnitures),
    path("about",views.about),
    path("contact",views.contact),
    path("testimonial",views.testimonial)
]