from django.urls import *
from .views import *


urlpatterns = [
    path('home/',view_home, name='home'),
    path('doctos/',view_doctos, name='doctos'),
    path('sevice/',view_service,name='service'),  #http:127.0.0.1:800/webasha/
    path('contact/',view_contact,name='contact'),
    path('ear/',view_ear, name='ear'),
    path('appointment/',view_appointment,name='appointment'),
]
