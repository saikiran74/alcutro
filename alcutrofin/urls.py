from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('favourite',views.favourite,name='favourite'),
    path('signin',views.signin,name='signin'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('chrome',views.chrome,name='chrome'),
    path('windows',views.windows,name='windows'),
    path('google',views.google,name='google'),
    path('microsoft',views.microsoft,name='microsoft'),
    path('youtube',views.youtube,name='youtube')
]