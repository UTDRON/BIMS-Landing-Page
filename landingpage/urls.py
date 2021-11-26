from django.contrib import admin
from django.urls import path, include
from landingpage import views

app_name = 'landingpage'


urlpatterns = [
    
    # path("",views.index, name='index'),
    path("",views.LandingPageView.as_view(), name='index'),
    # path("#testimonials/",views.contact,name='testimonials'),
    # path('list/', views.table_view, name='list'),
    path('list/', views.LandingPageListView.as_view(), name='list'),
    path('sms-otp/',views.sms_otp,name='sms-otp'),
    # if request coming from root urls.py matches this
    # blank request then go and run views.index function
    # path("home",views.index, name='home'),
    # path("about/",views.about, name='about'),
    # path("services/",views.services, name='services'),
    # path("contact/",views.contact, name='contact'),
]
