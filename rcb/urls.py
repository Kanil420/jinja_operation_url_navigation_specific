from django.urls import path
from rcb.views import *
app_name='rcbteam'

urlpatterns=[
    path('king/',king,name='king'),
]