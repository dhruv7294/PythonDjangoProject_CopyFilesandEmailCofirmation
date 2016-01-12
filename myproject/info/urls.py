from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.contact_form, name='contact'),
    url(r'^thanks/', views.thanks, name='thanks')

]
