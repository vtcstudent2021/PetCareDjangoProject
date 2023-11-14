from django.urls import path
from petapp import views


urlpatterns = [
    path('home/', views.home, name='home'), # home page url
    path('serivce/', views.serivce, name='serivce'), # serivce page url
    path('news/', views.news, name='news'), # news page url
    path('blog/', views.blog, name='blog'), # blog page url
    path('about/', views.about, name='about'), # about page url
    path('contact/', views.contact, name='contact'), # contact page url
    path('dialogflow/', views.dialogflow, name='dialogflow'), # dialogflow page url
    path('clinic_address/', views.clinic_address, name='clinic_address'), # dialogflow page url
]