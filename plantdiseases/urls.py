from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns=[ path('', views.home, name="home"),
              path('farmer',views.farmerscorner,name='farmer'),
              path('addf',views.addf,name='addf'),
              path('addc',views.addc,name='addc'),
              path('addp',views.addp,name='addp'),
              path('addfarmers',views.addfarmers,name='addfarmers'),
              path('addcrops',views.addcrops,name='addcrops'),
              path('addpests',views.addpests,name='addpests')
              ]